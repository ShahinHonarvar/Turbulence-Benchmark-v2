def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(circular_list)
    circular_list_extended = circular_list + circular_list
    results = []
    for length in range(1, n + 1):
        for start in range(n):
            sublist = circular_list_extended[start:start + length]
            if product(sublist) == -93:
                results.append(sublist)
    return results