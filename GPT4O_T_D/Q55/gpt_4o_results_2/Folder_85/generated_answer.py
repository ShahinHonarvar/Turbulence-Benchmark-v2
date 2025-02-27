def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == -97:
                result.append(circular_list[start:index + 1])
    return result