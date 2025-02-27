def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    extended_list = circular_list * 2
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = extended_list[start:start + length]
            if product(sublist) == -95:
                results.append(sublist)
    return results