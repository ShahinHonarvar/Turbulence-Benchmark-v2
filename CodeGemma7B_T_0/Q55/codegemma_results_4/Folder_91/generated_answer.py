def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i] * circular_list[j]
            if product == 2:
                return [[circular_list[i], circular_list[j]]]
    return []