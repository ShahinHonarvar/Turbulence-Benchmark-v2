def lists_with_product_equal_n(circular_list):
    target_product = 99
    result = []
    n = len(circular_list)
    extended_list = circular_list + circular_list[:-1]
    for start in range(n):
        product = 1
        sublist = []
        for end in range(start, start + n):
            product *= extended_list[end]
            sublist.append(extended_list[end])
            if product == target_product:
                result.append(sublist.copy())
            if product == 0 or product >= target_product:
                break
    return result