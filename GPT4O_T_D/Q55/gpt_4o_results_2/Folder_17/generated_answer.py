def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            end = (start + length) % n
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end]
            if product(sublist) == 18:
                results.append(sublist)
    return results