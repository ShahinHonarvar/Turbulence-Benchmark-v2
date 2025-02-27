def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    lst = lst + lst[:1]
    result = []
    for i in range(n * 2 - 1):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -8 and [lst[j % n] for j in range(i, i + n)] not in result:
                result.append([lst[j % n] for j in range(i, i + n)])
    return result