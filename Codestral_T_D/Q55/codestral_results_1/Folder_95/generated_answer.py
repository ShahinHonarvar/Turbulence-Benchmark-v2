def lists_with_product_equal_n(lst):
    n = 28
    res = []
    lst = lst + lst
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product > n:
                    break
                if product == n:
                    res.append(lst[i:j])
    return res