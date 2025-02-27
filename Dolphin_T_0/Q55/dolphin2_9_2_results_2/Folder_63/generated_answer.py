def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        for length in range(2, size + 1):
            product = 1
            for j in range(length):
                product *= lst[(i + j) % size]
            if product == 96:
                result.append(lst[i:i + length])
    return result