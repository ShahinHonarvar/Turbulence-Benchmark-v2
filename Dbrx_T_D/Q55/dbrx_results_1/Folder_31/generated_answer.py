def lists_with_product_equal_n(circular_list):
    n = -16
    result = []
    for i in range(len(circular_list)):
        sub_list = []
        current_product = 1
        for j in range(i, len(circular_list)):
            sub_list.append(circular_list[j])
            current_product *= circular_list[j]
            if current_product == n:
                result.append(sub_list.copy())
            elif current_product > n:
                break
    return result