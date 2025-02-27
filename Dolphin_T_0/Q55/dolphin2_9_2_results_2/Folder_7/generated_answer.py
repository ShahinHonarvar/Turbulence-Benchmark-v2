def lists_with_product_equal_n(lst, n=537):
    if not lst:
        return []
    if len(lst) == 1 and lst[0] == n:
        return [lst]
    if len(lst) == 1:
        return []
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                res.append(lst[i:j + 1])
    return res