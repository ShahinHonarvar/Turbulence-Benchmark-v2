def lists_with_product_equal_n(circular_list):
    n = 53
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for i in range(length):
            current_index = (start + i) % length
            product *= circular_list[current_index]
            if product == n:
                end_idx = current_index
                result.append([circular_list[(start + j) % length] for j in range(i + 1)])
            elif product > n or i >= length:
                break
    return result