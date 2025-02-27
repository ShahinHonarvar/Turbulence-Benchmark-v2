def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    product = 1
    lst_circular = lst + lst[:-1]
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst_circular[j]
            if product == 91:
                result.append(lst_circular[i:j + 1])
    return result