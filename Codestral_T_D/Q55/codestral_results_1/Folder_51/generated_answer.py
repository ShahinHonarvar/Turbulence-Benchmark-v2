def lists_with_product_equal_n(lst):
    lst = lst + lst
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -44:
                result.append(lst[i:j + 1])
    result = [list(x) for x in set((tuple(x) for x in result))]
    return result