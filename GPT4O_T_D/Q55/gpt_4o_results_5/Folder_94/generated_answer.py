def lists_with_product_equal_n(circular_list):
    n = -30
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for sub_list_length in range(1, length + 1):
            end = (start + sub_list_length - 1) % length
            product *= circular_list[end]
            if product == n:
                if start <= end:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
            elif product == 0:
                break
    return result