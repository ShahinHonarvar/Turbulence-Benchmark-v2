def lists_with_product_equal_n(circular_list):
    n = 93
    result = []
    for start in range(len(circular_list)):
        for end in range(start, len(circular_list) + start + 1):
            sublist = circular_list[start:end]
            if end > len(circular_list):
                sublist += circular_list[:end - len(circular_list)]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result