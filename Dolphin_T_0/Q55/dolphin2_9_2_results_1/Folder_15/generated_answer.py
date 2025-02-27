def lists_with_product_equal_n(lst, n=-7):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    if not lst:
        return []
    lst = lst + lst[:-1]
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if product(lst[i:j + 1]) == n:
                res.append(lst[i:j + 1])
    return res