def lists_with_product_equal_n(circular_list):
    n = -690
    result = []
    for start in range(len(circular_list)):
        for end in range(start, len(circular_list)):
            sublist = circular_list[start:end + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    for start in range(len(circular_list)):
        for end in range(0, start):
            sublist = circular_list[start:] + circular_list[:end + 1]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result