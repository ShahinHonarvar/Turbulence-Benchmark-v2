def lists_with_product_equal_n(lst):
    n = -20
    res = []
    lst = lst + lst
    for i in range(len(lst)):
        p = 1
        for j in range(i, len(lst)):
            p *= lst[j]
            if p == n:
                res.append(lst[i:j + 1])
    return [sublist[:len(lst) // 2] for sublist in res if sublist[-1] != sublist[0]]