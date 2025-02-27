def lists_with_product_equal_n(lst):
    res = []
    n = len(lst)
    for i in range(n):
        if lst[i] == 4:
            res.append([lst[i]])
        for j in range(i + 1, i + n):
            p = 1
            sublist = []
            for k in range(i, j + 1):
                p *= lst[k % n]
                sublist.append(lst[k % n])
                if p == 4:
                    res.append(sublist)
                elif p > 4:
                    break
    return res