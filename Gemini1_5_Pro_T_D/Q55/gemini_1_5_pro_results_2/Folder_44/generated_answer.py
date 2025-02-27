def lists_with_product_equal_n(circular_list):
    n = 29
    result = []
    for start in range(len(circular_list)):
        for end in range(start, start + len(circular_list)):
            sublist = circular_list[start:end % len(circular_list)] + circular_list[:end % len(circular_list) if end >= len(circular_list) else 0]
            if len(sublist) <= len(circular_list) and math.prod(sublist) == n:
                result.append(sublist)
    return result