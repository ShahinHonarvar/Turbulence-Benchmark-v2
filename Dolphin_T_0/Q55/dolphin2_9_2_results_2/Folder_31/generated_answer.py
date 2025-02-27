def lists_with_product_equal_n(lst):
    result = []
    lst = lst + lst[:1]
    for start in range(len(lst) - 1):
        for end in range(start + 1, len(lst)):
            if lst[start] * lst[end] == -16:
                result.append(lst[start:end + 1])
    return result