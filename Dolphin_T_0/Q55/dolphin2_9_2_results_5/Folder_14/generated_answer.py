def lists_with_product_equal_n(lst):
    if not lst:
        return []
    product = -72
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[i] * lst[j] == product and (j - i + 1 <= len(lst) or i > j):
                res.append(lst[i:j + 1])
    return res