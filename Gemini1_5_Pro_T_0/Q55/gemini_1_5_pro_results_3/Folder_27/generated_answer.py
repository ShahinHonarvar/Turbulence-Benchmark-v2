def lists_with_product_equal_n(circular_list):
    n = -82
    result = []
    for start in range(len(circular_list)):
        for end in range(start, start + len(circular_list)):
            sublist = circular_list[start:end + 1]
            if end >= len(circular_list):
                sublist += circular_list[:end - len(circular_list) + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result