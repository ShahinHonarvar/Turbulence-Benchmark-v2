def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for item in sublist:
            product *= item
        return product
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(1, n + 1):
            if end + start <= n:
                sublist = circular_list[start:start + end]
            else:
                sublist = circular_list[start:] + circular_list[:end + start - n]
            if product_of_sublist(sublist) == 42:
                result.append(sublist)
    return result