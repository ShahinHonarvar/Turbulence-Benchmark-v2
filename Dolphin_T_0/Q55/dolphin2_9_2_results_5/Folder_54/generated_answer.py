def lists_with_product_equal_n(lst):
    if len(lst) < 4:
        return []
    result = []
    p = -17
    for i in range(len(lst) - 1):
        if i >= 1 and i < len(lst) - 1 and (lst[i - 1] * lst[i] * lst[i + 1] == p) and (lst[i + 2] * lst[i + 3] != p):
            result.append([lst[i - 1], lst[i], lst[i + 1]])
        if i < len(lst) - 2 and lst[i] * lst[i + 1] * lst[i + 2] == p and (lst[i + 3] * lst[i + 4] != p):
            result.append([lst[i], lst[i + 1], lst[i + 2]])
    return result