def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for offset in range(length):
            product *= circular_list[(start + offset) % length]
            if product == -46:
                end = (start + offset) % length
                if start <= end:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
            if product == 0:
                break
    return result