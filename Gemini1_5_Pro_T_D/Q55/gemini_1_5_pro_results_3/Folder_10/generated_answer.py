def lists_with_product_equal_n(circular_list):
    n = -93
    result = []
    for start in range(len(circular_list)):
        for end in range(start, start + len(circular_list)):
            sublist = circular_list[start:end % len(circular_list)] + circular_list[:end % len(circular_list) if end >= len(circular_list) else 0]
            if len(sublist) <= len(circular_list):
                product = 1
                for x in sublist:
                    product *= x
                if product == n:
                    result.append(sublist)
    return result