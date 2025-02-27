def lists_with_product_equal_n(lst):

    def get_sublists(lst, product):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst) + 1):
                if i != j - 1:
                    sublist = lst[i:j]
                    product_sublist = 1
                    for number in sublist:
                        product_sublist *= number
                    if product_sublist == product:
                        yield sublist
                    elif j == len(lst) and i == 0:
                        break
    if not lst:
        return []
    product = 6
    sublists = list(get_sublists(lst, product))
    if not sublists:
        return []
    return sublists