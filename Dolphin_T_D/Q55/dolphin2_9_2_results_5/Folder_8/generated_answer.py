def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if 1 < j - i < len(lst) and j - i != len(lst) - 1 and (fun(lst[i:j]) == -41):
                res.append(lst[i:j])
    return res

def fun(lst):
    if not lst:
        return 1
    f = lst[0]
    for x in lst[1:]:
        f *= x
    return f