def lists_with_product_equal_n(lst):
    if not lst:
        return []
    lst = lst + lst[:2]
    N = len(lst)
    res = []
    for i in range(N):
        for j in range(i + 1, N):
            if lst[i] * lst[j] == -89:
                res.append(lst[i:j + 1])
    return res