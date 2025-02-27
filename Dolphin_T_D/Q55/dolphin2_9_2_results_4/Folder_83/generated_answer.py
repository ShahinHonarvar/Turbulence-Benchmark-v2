def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    res = []
    for i in range(len(lst)):
        if len(lst) == 1:
            return []
        elif lst[i] * lst[i + 1] == -57:
            res.append([lst[i], lst[i + 1]])
    res = list(set((tuple(sorted(sub)) for sub in res)))
    if len(lst) > 2:
        for i in range(len(lst) - 2):
            for j in range(i + 1, len(lst) - 1):
                if lst[i] * lst[i + 1] * lst[j] == -57:
                    res.append([lst[i], lst[i + 1], lst[j]])
        res = list(set((tuple(sorted(sub)) for sub in res)))
        if len(lst) > 3:
            for i in range(len(lst) - 3):
                for j in range(i + 1, len(lst) - 2):
                    for k in range(j + 1, len(lst) - 1):
                        if lst[i] * lst[i + 1] * lst[j] * lst[k] == -57:
                            res.append([lst[i], lst[i + 1], lst[j], lst[k]])
            res = list(set((tuple(sorted(sub)) for sub in res)))
    return res == [] and -57 not in lst or res