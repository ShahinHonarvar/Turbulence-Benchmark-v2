def lists_with_product_equal_n(lst, n=-65):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if i == j:
                continue
            product = 1
            for k in range(i, j):
                product *= lst[k % len(lst)]
            if product == n:
                res.append(lst[i:j])
    return res