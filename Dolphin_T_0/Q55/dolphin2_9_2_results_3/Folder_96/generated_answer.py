def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n_lst = len(lst)
    prefix = [1]
    for i in range(1, n_lst):
        prefix.append(prefix[i - 1] * lst[i - 1])
    suffix = [1]
    for i in range(n_lst - 1, -1, -1):
        suffix.insert(0, suffix[0] * lst[i])
    res = []
    m = 0
    if suffix[0] == 0:
        res.append(lst[:-1])
    for i in range(n_lst):
        if prefix[i] == 0 and suffix[i + 1] == 0:
            res.append(lst[m:i + 1])
            m = i + 1
    res.append(lst[m:])
    return res