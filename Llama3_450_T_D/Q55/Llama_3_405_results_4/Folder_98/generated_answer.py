def lists_with_product_equal_n(circular_list):
    result = []
    for _ in range(len(circular_list)):
        product = 1
        for j in range(len(circular_list)):
            product *= circular_list[j]
            if product == -1:
                result.append(circular_list[:j + 1])
        circular_list = circular_list[1:] + circular_list[:1]
    return result