def lists_with_product_equal_n(lst):
    if not lst:
        return []
    a = len(lst)
    res = []
    for i in range(a):
        for j in range(i, a + 1):
            if i != j:
                prod = 1
                for k in range(i, j):
                    prod *= lst[k]
                if prod == -18:
                    res.append(lst[i:j])
    return res