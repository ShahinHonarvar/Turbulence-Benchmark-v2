def lists_with_product_equal_n(circular_list):
    target_product = -30
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        for j in range(len(circular_list)):
            current_product *= circular_list[(i + j) % len(circular_list)]
            if current_product == target_product:
                result.append([circular_list[(i + k) % len(circular_list)] for k in range(j + 1)])
    return result