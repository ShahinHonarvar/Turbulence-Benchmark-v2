def lists_with_product_equal_n(l):
    n = len(l)
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            p = 1
            for k in range(i, j):
                p *= l[k]
                if p == -18:
                    sublists.append(l[i:j])
                    i = k
                    break
    return sublists