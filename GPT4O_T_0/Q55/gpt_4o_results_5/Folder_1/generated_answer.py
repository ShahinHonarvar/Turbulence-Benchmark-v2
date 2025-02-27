def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > n:
                sublist = circular_list[start:] + circular_list[:end % n]
            else:
                sublist = circular_list[start:end]
            if product_of_list(sublist) == -51:
                result.append(sublist)
    return result