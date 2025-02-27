def lists_with_product_equal_n(circular_list):

    def product_equals_zero(sublist):
        return 0 in sublist
    result = []
    n = len(circular_list)
    for start in range(n):
        for length in range(1, n + 1):
            end = (start + length - 1) % n
            if start <= end:
                sublist = circular_list[start:end + 1]
            else:
                sublist = circular_list[start:] + circular_list[:end + 1]
            if product_equals_zero(sublist):
                result.append(sublist)
    return result