def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        if lst[i] == 99:
            res.append([lst[i]])
        for j in range(i + 1, len(lst) + i):
            prod = 1
            sublist = []
            for k in range(i, j):
                prod *= lst[k % len(lst)]
                sublist.append(lst[k % len(lst)])
                if prod > 99:
                    break
                elif prod == 99:
                    res.append(sublist)
    return res