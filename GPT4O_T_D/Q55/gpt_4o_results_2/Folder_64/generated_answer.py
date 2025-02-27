def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for offset in range(n):
            index = (start + offset) % n
            product *= circular_list[index]
            if product == 3:
                end_index = (start + offset + 1) % n
                if end_index > index:
                    result.append(circular_list[start:index + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end_index])
            if product == 0 or product > 3:
                break
    return result