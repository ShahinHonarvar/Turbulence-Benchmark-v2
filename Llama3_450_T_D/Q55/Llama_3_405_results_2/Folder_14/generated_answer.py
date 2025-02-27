def lists_with_product_equal_n(circular_list):
    n = -72
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end % length]
            if product == n and start != end % length:
                sublist = circular_list[start:end % length + 1]
                if end % length < start:
                    sublist = circular_list[start:] + circular_list[:end % length + 1]
                result.append(sublist)
            if end != start and product > abs(n):
                break
    return result