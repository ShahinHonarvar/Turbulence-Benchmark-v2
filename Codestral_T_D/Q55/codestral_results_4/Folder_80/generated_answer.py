def lists_with_product_equal_n(lst):
    n = 43
    res = []
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst) + i):
            k = j % len(lst)
            p *= lst[k]
            if p == n:
                res.append(lst[i:k + 1] if i < k else lst[i:] + lst[:k + 1])
            if p > n:
                break
    return res