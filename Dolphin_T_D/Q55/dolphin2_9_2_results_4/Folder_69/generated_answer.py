def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    length = len(lst)
    sublists = []
    for i in range(length):
        product = 1
        for j in range(i, i + length):
            product *= lst[j % length]
            if product == 90:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(lst[k % length])
                sublists.append(sublist)
    return sublists