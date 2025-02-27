def lists_with_product_equal_n(circular_list):

    def product(seq):
        result = 1
        for num in seq:
            result *= num
        return result
    n = 100
    results = []
    length = len(circular_list)
    for start in range(length):
        for end in range(1, length + 1):
            if start <= end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if len(sublist) <= length and product(sublist) == n:
                results.append(sublist)
    return results