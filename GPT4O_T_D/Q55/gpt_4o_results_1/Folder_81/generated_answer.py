def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    sublists = []
    for length in range(1, n + 1):
        for start in range(n):
            end = start + length
            if end <= n:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end % n]
            if product(sublist) == -8:
                sublists.append(sublist)
    return sublists