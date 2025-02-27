def lists_with_product_equal_n(circular_list):

    def product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    list_length = len(circular_list)
    for size in range(1, list_length + 1):
        for start in range(list_length):
            sublist = circular_list[start:start + size]
            if product_equal_n(sublist) == 42:
                result.append(sublist)
    return result