def lists_with_product_equal_n(circular_list):
    target_product = -56
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == target_product:
                result.append(circular_list[i:i + j + 1])
            elif product == 0:
                break
    return result