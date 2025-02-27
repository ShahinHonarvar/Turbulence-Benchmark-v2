def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i + j) % size]
            if product == 57:
                result.append(lst[(i + j) % size])
                if j > 0:
                    for k in range(i, i + j):
                        result.append(lst[k])
    return result