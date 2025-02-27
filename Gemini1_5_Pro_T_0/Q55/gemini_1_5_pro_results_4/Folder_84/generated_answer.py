def lists_with_product_equal_n(circular_list):
    n = -906
    result = []
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list) + 1):
            sublist = circular_list[start:end]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list)):
            sublist = circular_list[start:] + circular_list[:end]
            product = 1
            for num in sublist:
                product *= num
            if product == n:
                result.append(sublist)
    return result