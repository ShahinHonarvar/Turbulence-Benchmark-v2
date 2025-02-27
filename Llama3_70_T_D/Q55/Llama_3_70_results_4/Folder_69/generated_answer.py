def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(size):
            product *= lst[(i + j) % size]
            if product > 90:
                break
            if product == 90:
                result.append(lst[(i + j) % size:])
    return result