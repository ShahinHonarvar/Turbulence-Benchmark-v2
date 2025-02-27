def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(circular_list)
    results = []
    for start in range(n):
        for size in range(1, n + 1):
            end = (start + size) % n
            if end > start:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == -10:
                results.append(sublist)
    return results