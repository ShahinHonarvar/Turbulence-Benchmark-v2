def lists_with_product_equal_n(circular_list):

    def product_equal_990(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 990
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j] % n
            if product_equal_990(sublist):
                result.append(sublist)
    return result