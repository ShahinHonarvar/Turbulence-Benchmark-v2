def lists_with_product_equal_n(lst):
    lst = lst + lst[:1]
    result = []
    for start in range(len(lst)):
        for end in range(start + 1, len(lst)):
            if lst[start] * lst[end] == 57:
                result.append(lst[start:end + 1])
    return result if result else []