def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        for length in range(1, size + 1):
            product *= circular_list[(start + length - 1) % size]
            if product == -41:
                end = (start + length) % size
                if start < end:
                    result.append(circular_list[start:end])
                else:
                    result.append(circular_list[start:] + circular_list[:end])
            if length == size:
                break
    return result