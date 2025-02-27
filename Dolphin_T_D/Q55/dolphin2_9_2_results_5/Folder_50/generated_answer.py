def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 45:
                sublist = lst[i:j % n + 1]
                if sublist != sublists:
                    sublists.append(sublist)
    return sublists