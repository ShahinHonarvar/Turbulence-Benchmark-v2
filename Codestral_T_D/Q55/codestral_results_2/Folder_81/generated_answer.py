def lists_with_product_equal_n(lst):
    lst *= 2
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -8:
                sublists.append(lst[i:j + 1])
    return sublists