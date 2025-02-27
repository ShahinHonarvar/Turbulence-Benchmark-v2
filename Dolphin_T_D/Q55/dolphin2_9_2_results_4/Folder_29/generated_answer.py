def lists_with_product_equal_n(lst):
    if not lst:
        return []
    size = len(lst)
    lst = lst + lst[:size // 2]
    sublists = []
    for i in range(size):
        product = 1
        temp = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product > 15:
                break
            if product == 15:
                sublist = lst[i:j + 1]
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists