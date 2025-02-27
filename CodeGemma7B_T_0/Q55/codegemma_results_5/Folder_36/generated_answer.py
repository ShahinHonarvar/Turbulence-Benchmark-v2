def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == 714:
                return [circular_list[i:j + 1]]
            elif product > 714:
                break
    return []