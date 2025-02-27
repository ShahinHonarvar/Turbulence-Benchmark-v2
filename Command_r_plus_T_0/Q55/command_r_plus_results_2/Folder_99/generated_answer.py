def lists_with_product_equal_n(circular_list):

    def product_equal_n(start, length):
        product = 1
        for i in range(length):
            product *= circular_list[(start + i) % len(circular_list)]
        return product == 415
    result = []
    for i in range(len(circular_list)):
        for j in range(1, len(circular_list) + 1):
            if product_equal_n(i, j):
                result.append(circular_list[i:i + j])
    return result