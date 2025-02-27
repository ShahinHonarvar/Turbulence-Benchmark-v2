def lists_with_product_equal_n(lst):
    result = []
    if len(lst) == 0:
        return result
    if len(lst) == 1 and lst[0] == 32:
        result.append([lst[0]])
        return result
    for i in range(len(lst)):
        different = 32 // lst[i]
        if different in lst[i + 1:] or different in lst[:i]:
            if lst[i] != 1 and different != 1:
                result.append([lst[i], different])
            if different == 1 and len(lst) == 1:
                result.append([lst[i]])
    return result