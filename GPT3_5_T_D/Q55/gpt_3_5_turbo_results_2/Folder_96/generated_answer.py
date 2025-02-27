def lists_with_product_equal_n(circular_list):
    sublists = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for start in range(n):
            sublist = circular_list[start:start + length]
            if not sublist or 0 in sublist:
                sublists.append(sublist)
    return sublists