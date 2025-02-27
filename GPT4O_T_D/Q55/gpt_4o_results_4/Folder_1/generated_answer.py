def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        current_sublist = []
        for i in range(n):
            current_index = (start + i) % n
            product *= circular_list[current_index]
            current_sublist.append(circular_list[current_index])
            if product == -51:
                result.append(current_sublist[:])
            elif abs(product) > abs(-51) or product == 0:
                break
    return result