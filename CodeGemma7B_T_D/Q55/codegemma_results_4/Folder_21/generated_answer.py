def lists_with_product_equal_n(lst):
    p = 1
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if p * lst[j] > 851:
                break
            p *= lst[j]
            if p == 851:
                res.append(lst[i:j + 1])
    return res