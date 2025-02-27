def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= lst[k]
            if prod == -3:
                result.append(lst[i:j + 1])
        for j in range(0, i + 1):
            prod = 1
            for k in range(i, n):
                prod *= lst[k]
            for k in range(0, j + 1):
                prod *= lst[k]
            if prod == -3:
                result.append(lst[i:] + lst[:j + 1])
    return result