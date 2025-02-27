def lists_with_product_equal_n(circular_list):
    target_product = -837
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == target_product:
                result.append([circular_list[(i + k) % len(circular_list)] for k in range(j + 1)])
            elif product > target_product or j == len(circular_list) - 1:
                break
    return result