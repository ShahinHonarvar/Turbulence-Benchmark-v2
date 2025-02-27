def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    lst = lst + lst[:1]
    result = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] * lst[j] == 57:
                result.append(lst[i:j + 1])
    return result