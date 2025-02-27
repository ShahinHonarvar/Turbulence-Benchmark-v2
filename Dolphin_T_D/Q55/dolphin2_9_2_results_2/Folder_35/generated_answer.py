def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    product = 1
    for i in range(size):
        product *= lst[i]
    if product != 83:
        return result
    for i in range(size):
        product_i = 1
        for j in range(i, size):
            product_i *= lst[j]
            if product_i == 83:
                result.append(lst[i:j + 1])
    return result