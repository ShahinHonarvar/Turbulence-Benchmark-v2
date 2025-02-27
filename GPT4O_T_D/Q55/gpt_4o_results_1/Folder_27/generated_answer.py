def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -82
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= circular_list[end % n]
            if current_product == target_product:
                result.append([circular_list[i % n] for i in range(start, end + 1)])
            if abs(current_product) > abs(target_product) and current_product != 0:
                break
    return result