def lists_with_product_equal_n(circular_list):
    result = []
    n = 74
    length = len(circular_list)
    for start in range(length):
        product = 1
        sub_list = []
        for i in range(length):
            current_index = (start + i) % length
            sub_list.append(circular_list[current_index])
            product *= circular_list[current_index]
            if product == n:
                result.append(sub_list[:])
            if len(sub_list) >= length or product > n:
                break
    return result