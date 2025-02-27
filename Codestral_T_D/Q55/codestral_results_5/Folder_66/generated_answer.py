def lists_with_product_equal_n(lst):
    n = 78
    res = []
    lst += lst
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            pr = 1
            sub = []
            for k in range(i, j + 1):
                pr *= lst[k]
                sub.append(lst[k])
                if pr > n:
                    break
                elif pr == n:
                    res.append(sub)
    return [sublist for sublist in res if len(sublist) <= len(lst) // 2]