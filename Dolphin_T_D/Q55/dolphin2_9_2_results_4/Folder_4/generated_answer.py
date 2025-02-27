def lists_with_product_equal_n(lst):
    if not all((isinstance(i, int) for i in lst)):
        return []
    if len(lst) < 2:
        return []
    lst = lst + lst[:2]
    n = 91
    sublists = []
    for i in range(len(lst) - 1):
        product = lst[i]
        if product == n:
            sublists.append([lst[i]])
        sublists_temp = []
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == n:
                sublists_temp.append(lst[i:j + 1])
            elif product > n:
                break
    sublists.extend(sublists_temp)
    return sublists