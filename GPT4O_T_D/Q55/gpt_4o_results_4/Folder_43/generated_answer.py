def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    results = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > start:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == -26:
                results.append(sublist)
    return results