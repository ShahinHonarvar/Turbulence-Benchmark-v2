def lists_with_product_equal_n(circular_list):

    def product_equal_53(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 53
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if product_equal_53(sublist):
                result.append(sublist)
    return result