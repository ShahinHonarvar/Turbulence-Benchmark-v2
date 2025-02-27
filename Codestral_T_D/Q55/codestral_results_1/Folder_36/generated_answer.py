def lists_with_product_equal_n(lst):
    n = 714
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[(j + i) % len(lst)]
            if prod == n:
                res.append(lst[i:j + 1])
            elif prod > n:
                break
        if lst[i] == n:
            res.append([lst[i]])
    return res