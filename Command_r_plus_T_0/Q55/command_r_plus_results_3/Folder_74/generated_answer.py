def lists_with_product_equal_n(circular_list):

    def product_equal_51(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 51
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i + 1):
            sublist = circular_list[i:j % len(circular_list)]
            if product_equal_51(sublist):
                result.append(sublist)
    return result