def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst
    result = []
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod *= lst[j]
            if prod == 37:
                result.append(lst[i:j + 1])
            if prod > 37:
                break
    return result