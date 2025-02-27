def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for number in sublist:
            result *= number
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            idx_start = start
            idx_end = end if end <= n else end - n
            if idx_end <= idx_start:
                sublist = circular_list[idx_start:] + circular_list[:idx_end]
            else:
                sublist = circular_list[idx_start:idx_end]
            if product(sublist) == 415:
                result.append(sublist)
    return result