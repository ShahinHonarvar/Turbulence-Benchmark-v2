def lists_with_product_equal_n(circular_list):
    target_product = -16
    result = []
    for i in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[(i + j) % len(circular_list)]
            if product == target_product:
                result.append(circular_list[i:i + j + 1] if i + j + 1 <= len(circular_list) else circular_list[i:] + circular_list[:j - len(circular_list) + i + 1])
            elif product == 0 or abs(product) > abs(target_product):
                break
    return result