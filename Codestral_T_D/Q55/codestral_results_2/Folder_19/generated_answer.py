def lists_with_product_equal_n(lst):
    lst *= 2
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == -54:
                result.append(lst[i:j + 1])
    return result