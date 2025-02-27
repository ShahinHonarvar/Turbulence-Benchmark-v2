def lists_with_product_equal_n(lst):
    n = -3
    res = []
    for i in range(len(lst)):
        if lst[i] == n:
            res.append([lst[i]])
        elif lst[i] == 0:
            continue
        else:
            prod = lst[i]
            sublist = [lst[i]]
            for j in range(i + 1, len(lst) + i):
                prod *= lst[j % len(lst)]
                sublist.append(lst[j % len(lst)])
                if prod == n:
                    res.append(sublist)
                elif abs(prod) < abs(n):
                    break
    return res