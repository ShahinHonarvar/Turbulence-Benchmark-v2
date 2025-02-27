def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == 415:
                return [circular_list[i:j + 1]]
            elif product > 415:
                break
    return []