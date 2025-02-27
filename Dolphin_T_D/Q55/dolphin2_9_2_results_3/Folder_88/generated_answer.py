def lists_with_product_equal_n(lst):
    if len(lst) < 2:
        return []
    res = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == -56:
                if j - i + 1 < len(lst) and lst[i] != lst[j + 1]:
                    for k in range(i + 1, j + 1):
                        if lst[i] == lst[k]:
                            break
                        sublist = [lst[i]]
                        for m in range(k + 1, j + 1):
                            sublist.append(lst[m])
                        res.append(sublist)
    return res