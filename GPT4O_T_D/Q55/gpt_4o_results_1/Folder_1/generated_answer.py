def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    size = len(circular_list)
    results = []
    extended_list = circular_list + circular_list[:-1]
    for start in range(size):
        for end in range(start + 1, start + size + 1):
            sublist = extended_list[start:end]
            if product(sublist) == -51:
                results.append(sublist)
    return results