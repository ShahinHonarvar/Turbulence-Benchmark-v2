def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        prod = 1
        for j in range(i, i + size):
            prod *= lst[j % size]
            if prod == 93:
                result.append(lst[i:j % size + 1])
    return result