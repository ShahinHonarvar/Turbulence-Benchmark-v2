def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        temp_list = []
        for i in range(n):
            current_index = (start + i) % n
            product *= circular_list[current_index]
            temp_list.append(circular_list[current_index])
            if product == 714:
                result.append(temp_list[:])
                break
            elif product > 714:
                break
    return result