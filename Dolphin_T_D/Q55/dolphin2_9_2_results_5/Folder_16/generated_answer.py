def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == -837:
                result.append(lst[i:j + 1])
    return result