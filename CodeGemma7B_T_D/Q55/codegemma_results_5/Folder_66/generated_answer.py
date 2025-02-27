def lists_with_product_equal_n(lst):
    """
            Last
            """
    product = 1
    '\n            Is this valid? Making sure the list contains at least three integers\n            '
    if len(lst) < 3:
        return []
    '\n            This could be done with a dictionary as well, but I like the order of this for-loop\n            '
    for i, integer in enumerate(lst):
        product *= integer
    '\n            Reverse the list\n            '
    lst.reverse()
    '\n            For loop starting from the end of the reversed list. \n            Because the end of the list contains the greatest numbers and we are multiplying\n            '
    for i in range(len(lst)):
        '\n                For each integer, reverse the list from its index to the beginning of the list\n                '
        lst.reverse()
        for j in range(i, len(lst)):
            '\n                    If the product of the integers from the index of the outermost loop to the end of the list is equal to the target product (78)\n                    '
            if j == len(lst) - 1:
                if product / lst[i] == 78:
                    '\n                            If the list is not yet in the returned list, append it\n                            '
                    if lst[:j + 1] not in res:
                        res.append(lst[:j + 1])
            else:
                product *= lst[j + 1]
    '\n            Reverse the list again to go back to normal order\n            '
    lst.reverse()
    '\n            If the result list is empty, return an empty list\n            '
    if res == []:
        return []
    else:
        return res