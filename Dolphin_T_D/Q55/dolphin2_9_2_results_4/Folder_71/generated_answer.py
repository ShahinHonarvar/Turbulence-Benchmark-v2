def lists_with_product_equal_n(lst):
    size = len(lst)
    result = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k % size]
            if product == 47:
                result.append(lst[i:j])
    return result