def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if i == 0 and j == len(lst) - 1:
                prod = lst[i] * lst[j]
            else:
                prod = lst[i] * lst[j - 1]
            if prod == -41 or prod == -41.0:
                new = []
                for k in range(i, j):
                    new.append(lst[k])
                res.append(new)
    return res