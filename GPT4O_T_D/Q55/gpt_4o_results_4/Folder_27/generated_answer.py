def lists_with_product_equal_n(circular_list):
    target_product = -82
    n = len(circular_list)
    result = []
    if n == 0:
        return result
    extended_list = circular_list + circular_list
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == 0:
                break
            if product == target_product:
                result.append(extended_list[start:end + 1])
    return result