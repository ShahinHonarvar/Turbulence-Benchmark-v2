def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst) * 2):
            idx = j % len(lst)
            sublist.append(lst[idx])
            product *= lst[idx]
            if product == 43:
                result.append(sublist)
    return result