def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    elif n == 1:
        return [lst] if lst[0] == 36 else []
    lst_circular = lst + lst[:-1]
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst_circular[j]
            if product == 36:
                result.append(lst_circular[i:j + 1])
    return result