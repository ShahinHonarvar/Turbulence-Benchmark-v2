def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    extended_list = circular_list * 2
    for start in range(n):
        for size in range(1, n + 1):
            sublist = extended_list[start:start + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -36:
                result.append(sublist)
    return result