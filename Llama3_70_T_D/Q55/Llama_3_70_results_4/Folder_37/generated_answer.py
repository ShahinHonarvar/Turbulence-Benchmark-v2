def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for window_size in range(1, n + 1):
        for i in range(n):
            sublist = circular_list[i:i + window_size]
            if len(sublist) < n and len(sublist) > 0:
                if i + window_size > n:
                    sublist += circular_list[:i + window_size - n]
                if sublist[0] * sublist[1] == -76:
                    result.append(sublist)
    return result