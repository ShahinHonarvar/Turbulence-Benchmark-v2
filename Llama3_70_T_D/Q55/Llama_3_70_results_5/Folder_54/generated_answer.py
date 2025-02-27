def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for window_size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + window_size]
            if i + window_size > n:
                sublist += circular_list[:i + window_size - n]
            product = 1
            for num in sublist:
                product *= num
            if product == -17:
                result.append(sublist)
    return result