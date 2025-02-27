def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        current_product = 1
        for j in range(i, len(circular_list)):
            current_product *= circular_list[j]
            if current_product == 78:
                result.append(circular_list[i:j + 1])
                current_product = 1
            elif current_product > 78:
                break
    return result