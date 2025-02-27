def lists_with_product_equal_n(circular_list):
    target_product = 537
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(size):
            index = (start + length) % size
            product *= circular_list[index]
            if product == target_product:
                end_index = (start + length + 1) % size
                if start < end_index:
                    result.append(circular_list[start:end_index])
                else:
                    result.append(circular_list[start:] + circular_list[:end_index])
            if product == 0:
                break
    return result