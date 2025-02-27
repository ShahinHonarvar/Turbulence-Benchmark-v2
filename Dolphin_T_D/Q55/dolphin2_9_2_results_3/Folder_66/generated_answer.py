def product_equal_n(lst, n):
    if n == 1:
        return [[]]
    res = []
    for i in range(len(lst)):
        if lst[i] == 1:
            res.append([1])
        elif lst[i] % n == 0:
            res.append([lst[i]])
        else:
            for j in range(i + 1, len(lst)):
                if lst[i] * lst[j] % n == 0:
                    res.append([lst[i], lst[j]])
    return res

def lists_with_product_equal_n(lst):
    lst = lst + lst[:-1]
    res = []
    for i in range(len(lst)):
        for sub_res in product_equal_n(lst[i:], 78):
            if len(sub_res) <= len(lst):
                res.append(sub_res)
    return res