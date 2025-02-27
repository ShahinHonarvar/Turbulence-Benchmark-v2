def lists_with_product_equal_n(circular_list):
    target_product = -906
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            idx = end % length
            product *= circular_list[idx]
            if product == target_product:
                result.append([circular_list[i % length] for i in range(start, end + 1)])
            if product == 0:
                break
    return result