def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for size in range(1, length + 1):
        for i in range(length):
            product = 1
            for j in range(size):
                product *= lst[(i + j) % length]
            if product == -57:
                result.append([lst[(i + k) % length] for k in range(size)])
    return result