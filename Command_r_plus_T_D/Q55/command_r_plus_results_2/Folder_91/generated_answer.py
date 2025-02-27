def lists_with_product_equal_n(circular_list):

    def check_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 2
    result = []
    for i in range(len(circular_list)):
        for j in range(i, i + len(circular_list)):
            sublist = circular_list[i:j]
            if check_product(sublist):
                result.append(sublist)
    return result