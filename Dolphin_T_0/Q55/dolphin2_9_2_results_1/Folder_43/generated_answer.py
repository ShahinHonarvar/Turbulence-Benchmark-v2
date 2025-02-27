def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst[:-1]
    sublists = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product == -26:
                sublists.append(lst[i:j + 1])
    return sublists