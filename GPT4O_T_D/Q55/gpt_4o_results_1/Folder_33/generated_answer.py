def lists_with_product_equal_n(circular_list):
    target_product = -115
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == target_product:
                result.append(extended_list[start:end + 1])
    return result