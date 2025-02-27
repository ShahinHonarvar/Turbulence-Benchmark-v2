def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == -57:
                result.append(circular_list[(i + j) % len(circular_list)])
            elif product < -57:
                break
    return [item for sublist in result for item in [sublist] * sublist.count(item)]