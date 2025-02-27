def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end % n]
            if product == -81:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
    return result