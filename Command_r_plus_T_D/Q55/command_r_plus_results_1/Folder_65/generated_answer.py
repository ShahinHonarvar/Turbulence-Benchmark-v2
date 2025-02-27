def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(i, n + i):
            sublist = circular_list[i:j] % n
            if product(sublist) == 46:
                result.append(sublist)
    return result