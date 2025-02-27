def lists_with_product_equal_n(circular_list):
    target_product = -690
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        current_product = 1
        sublist = []
        for offset in range(list_size):
            index = (start + offset) % list_size
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == target_product:
                result.append(sublist.copy())
            if current_product == 0 or current_product == target_product:
                break
            if abs(current_product) > abs(target_product):
                break
    return result