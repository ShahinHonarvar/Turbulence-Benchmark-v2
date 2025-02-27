def lists_with_product_equal_n(circular_list):
    n = 632
    result = []
    for start in range(len(circular_list)):
        for end in range(start + 1, len(circular_list) + 1):
            sublist = circular_list[start:end]
            product = 1
            for x in sublist:
                product *= x
            if product == n:
                result.append(sublist)
    return result