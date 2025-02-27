def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1 and lst[0] != -91:
        return []
    result = []
    multi = 1
    for i in range(len(lst)):
        multi *= lst[i]
        if multi == -91:
            result.append(lst[:i + 1])
        if multi > -91:
            multi = 1
    return result