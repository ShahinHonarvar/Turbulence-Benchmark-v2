def lists_with_product_equal_n(lst, n=-44):
    if not lst:
        return []
    lst = lst + [lst[0]]
    res = []
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
        if prod == n:
            temp = [lst[i]]
            prod = 1
            for j in range(i + 1, len(lst)):
                prod *= lst[j]
                temp.append(lst[j])
                if prod == n:
                    res.append(temp)
    if not res:
        return []
    return res