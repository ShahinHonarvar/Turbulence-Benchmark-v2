def lists_with_product_equal_n(lst):
    n = 8
    size = len(lst)
    res = []
    for i in range(size):
        if lst[i] == n:
            res.append([lst[i]])
        prod = lst[i]
        for j in range(i + 1, i + size):
            prod *= lst[j % size]
            if prod == n:
                res.append(lst[i:j % size + 1])
            if prod > n:
                break
    return res