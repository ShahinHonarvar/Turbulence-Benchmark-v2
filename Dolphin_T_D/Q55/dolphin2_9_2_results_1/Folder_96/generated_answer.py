def lists_with_product_equal_n(lst):
    n = len(lst)
    a, b = ([1] * n, [1] * n)
    lst.append(0)
    for i in range(n - 1, -1, -1):
        a[i] = a[i + 1] * lst[i]
    for i in range(n):
        b[i] = b[i - 1] * lst[i - 1]
    res = []
    for i in range(n):
        for j in range(n + 1):
            if a[j] * b[i] == 0:
                res.append(lst[j:i + j])
    return res