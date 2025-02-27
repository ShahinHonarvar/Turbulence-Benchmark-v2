def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    if n == 1:
        return [lst] if lst[0] == 45 else []
    sublists = []
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == 45:
            sublists.append(lst[:i + 1])
        if i < n - 1:
            product //= lst[i + 1]
    for start in range(1, n):
        product = lst[start - 1]
        for end in range(start, n):
            product *= lst[end]
            if product == 45:
                sublists.append(lst[start - 1:end + 1])
    return sublists