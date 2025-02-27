def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in range(j + 1, len(circular_list)):
                product *= circular_list[k]
            if product == -3:
                return [[circular_list[i], circular_list[j], circular_list[k]]]
    return []