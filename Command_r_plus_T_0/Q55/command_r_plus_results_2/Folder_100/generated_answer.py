def lists_with_product_equal_n(circular_list):

    def product_equal_48(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 48
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(i + 1, length + i + 1):
            sublist = circular_list[i:j % length]
            if product_equal_48(sublist):
                result.append(sublist)
    return result