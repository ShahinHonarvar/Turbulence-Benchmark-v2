def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    product = 1
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= lst[j % size]
            if product == -18:
                result.append(lst[i:j % size + 1])
    return result