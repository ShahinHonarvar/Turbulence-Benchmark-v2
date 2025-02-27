def lists_with_product_equal_n(circular_list):
    n = 74
    result = []
    for i in range(len(circular_list)):
        product = 1
        current_list = []
        for j in range(len(circular_list)):
            index = (i + j) % len(circular_list)
            product *= circular_list[index]
            current_list.append(circular_list[index])
            if product == n:
                result.append(current_list.copy())
    return result