def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = 47
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) * 2):
            index = j % len(lst)
            product *= lst[index]
            if product == n:
                sublist = lst[i:index + 1]
                sublists.append(sublist)
    return sublists