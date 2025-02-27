def lists_with_product_equal_n(circular_list):
    product = -89
    result = []
    for start in range(len(circular_list)):
        current_product = circular_list[start]
        sublist = [circular_list[start]]
        for end in range(start + 1, len(circular_list)):
            current_product *= circular_list[end]
            sublist.append(circular_list[end])
            if current_product == product:
                result.append(sublist[:])
            if current_product > product:
                break
    return result