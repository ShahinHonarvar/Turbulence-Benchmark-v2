def lists_with_product_equal_n(circular_list):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > n:
                sublist = circular_list[start:] + circular_list[:end % n]
            else:
                sublist = circular_list[start:end]
            if len(sublist) > n:
                continue
            if product(sublist) == 78:
                result.append(sublist)
    return result