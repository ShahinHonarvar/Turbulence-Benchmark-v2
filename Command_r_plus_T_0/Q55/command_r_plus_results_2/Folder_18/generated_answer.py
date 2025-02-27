def lists_with_product_equal_n(circular_list):

    def product_equal_36(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 36
    length = len(circular_list)
    result = []
    for size in range(1, length + 1):
        for start in range(length):
            sublist = circular_list[start:start + size]
            if product_equal_36(sublist):
                result.append(sublist)
    return result