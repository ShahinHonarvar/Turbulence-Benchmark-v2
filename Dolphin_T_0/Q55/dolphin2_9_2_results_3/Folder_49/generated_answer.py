def lists_with_product_equal_n(lst, n=-61):
    if not lst:
        return []
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                res.append(lst[i:j + 1])
            elif product > n:
                break
    for i in range(1, len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                res.append(lst[0:i] + lst[j:])
            elif product > n:
                break
    return res