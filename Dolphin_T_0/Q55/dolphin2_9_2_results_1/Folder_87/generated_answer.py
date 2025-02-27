def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    if size == 0:
        return result
    product_index = {}
    product = 1
    for i in range(size):
        product_index[i] = product
        product *= lst[i]
    product *= lst[0]
    for i in range(size):
        product_contiguous = 1
        for j in range(i, size):
            product_contiguous *= lst[j]
            if product_contiguous == 27:
                result.append(lst[i:j + 1])
    return result