def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i + j) % size]
            if product == -906:
                result.append(lst[(i + j) % size])
                for k in range(1, j + 1):
                    result.append(lst[(i + j - k) % size])
    return result