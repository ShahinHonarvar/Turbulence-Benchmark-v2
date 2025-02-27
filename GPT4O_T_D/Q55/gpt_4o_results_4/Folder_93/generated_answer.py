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
            if start + end <= n:
                sublist = circular_list[start:start + end]
            else:
                sublist = circular_list[start:] + circular_list[:start + end - n]
            if product_of_list(sublist) == -91:
                result.append(sublist)
    return result