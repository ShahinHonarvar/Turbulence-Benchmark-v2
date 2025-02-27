def lists_with_product_equal_n(circular_list):
    n = 96
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == n:
                end_index = end + 1
                if end_index > length:
                    result.append(circular_list[start:] + circular_list[:end_index % length])
                else:
                    result.append(circular_list[start:end_index])
            if product == 0 or product > n:
                break
    return result