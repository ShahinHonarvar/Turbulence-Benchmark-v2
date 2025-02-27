def lists_with_product_equal_n(circular_list):
    circular_list = circular_list * 2
    size = len(circular_list) // 2
    result = []
    for i in range(size):
        product = 1
        for j in range(i, size + i):
            product *= circular_list[j]
            if product == -36:
                result.append(circular_list[i:j + 1])
    return result