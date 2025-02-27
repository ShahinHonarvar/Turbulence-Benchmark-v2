def lists_with_product_equal_n(lst):
    result = []
    lst = lst + lst
    for i in range(len(lst) - 1):
        prod = 1
        for j in range(i + 1, len(lst)):
            prod *= lst[j]
            if prod == 33 and len(lst[i:j + 1]) <= len(lst) // 2:
                result.append(lst[i:j + 1])
    return result