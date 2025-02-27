def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    prefix_product = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_product[i] = prefix_product[i - 1] * lst[i - 1]
    result = []
    for i in range(n):
        for j in range(i, n):
            product = prefix_product[j + 1]
            if i > 0:
                product //= prefix_product[i]
            if product == -72:
                result.append(lst[i:j + 1])
    return result