def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] == 4:
            res.append([lst[i]])
        for j in range(i + 1, len(lst)):
            prod = lst[i]
            sublist = [lst[i]]
            for k in range(i + 1, j + 1):
                prod *= lst[k]
                sublist.append(lst[k])
                if prod == 4:
                    res.append(sublist)
    return res