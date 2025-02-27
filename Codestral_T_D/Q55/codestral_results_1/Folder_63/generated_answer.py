def lists_with_product_equal_n(circular_list):
    n = 96
    size = len(circular_list)
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j % size]
            if product == n:
                result.append(circular_list[i:j % size + 1])
            if product > n:
                break
    return result