def lists_with_product_equal_n(circular_list):

    def product_equal_eight(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 8
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j]
            if product_equal_eight(sublist):
                result.append(sublist)
    return result