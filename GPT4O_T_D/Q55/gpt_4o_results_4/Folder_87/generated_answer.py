def lists_with_product_equal_n(circular_list):
    n = 27
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            index = end % length
            product *= circular_list[index]
            if product == n:
                if end >= length:
                    result.append(circular_list[start:] + circular_list[:index + 1])
                else:
                    result.append(circular_list[start:index + 1])
            if product == 0 or product > n:
                break
    return result