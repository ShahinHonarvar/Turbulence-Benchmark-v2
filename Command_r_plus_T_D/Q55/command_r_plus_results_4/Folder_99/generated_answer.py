def lists_with_product_equal_n(circular_list):

    def product_equal_n(start, length):
        product = 1
        for i in range(start, start + length):
            product *= circular_list[i % len(circular_list)]
        return product == 415
    n = len(circular_list)
    result = []
    for length in range(1, n + 1):
        for start in range(n):
            if product_equal_n(start, length):
                result.append(circular_list[start:start + length])
    return result