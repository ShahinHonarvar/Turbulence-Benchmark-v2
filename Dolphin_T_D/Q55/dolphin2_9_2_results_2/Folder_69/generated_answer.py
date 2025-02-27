def lists_with_product_equal_n(lst, n=90):
    if not lst or (lst and len(lst) == 1 and (lst[0] != 1) and (lst[0] != -1)):
        return []
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n and [lst[i:j + 1]] not in res:
                res.append([lst[i:j + 1]])
    for i in range(len(lst)):
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == n and [lst[j:i + 1]] not in res:
                res.append([lst[j:i + 1]])
    return res