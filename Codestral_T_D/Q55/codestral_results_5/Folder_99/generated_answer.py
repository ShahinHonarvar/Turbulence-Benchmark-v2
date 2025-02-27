def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst = lst + lst
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= lst[j]
            if prod == 415:
                result.append(lst[i:j + 1])
            if prod > 415:
                break
    return result