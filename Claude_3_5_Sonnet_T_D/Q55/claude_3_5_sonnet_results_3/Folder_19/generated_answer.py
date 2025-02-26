def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for start in range(n):
        for size in range(1, n + 1):
            sublist = extended_list[start:start + size]
            product = 1
            for num in sublist:
                product *= num
            if product == -54:
                result.append(sublist)
    return result