def lists_with_product_equal_n(lst):
    n = len(lst)
    res = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            if i != j and j != i + n:
                product = 1
                for k in range(i, j):
                    product *= lst[k]
                if product == -10:
                    res.append(lst[i:j])
    return res