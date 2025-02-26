def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = extended_list[start:end]
            product = 1
            for num in sublist:
                product *= num
            if product == -91:
                result.append(sublist)
    return result