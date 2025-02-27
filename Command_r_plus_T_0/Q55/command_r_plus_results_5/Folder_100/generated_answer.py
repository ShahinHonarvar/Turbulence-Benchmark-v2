def lists_with_product_equal_n(circular_list):

    def product_equal_48(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 48
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j]
            if product_equal_48(sublist):
                result.append(sublist)
    return result