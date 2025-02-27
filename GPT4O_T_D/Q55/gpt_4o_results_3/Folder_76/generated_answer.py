def lists_with_product_equal_n(circular_list):

    def product_equals_247(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == 247
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for offset in range(length):
                sublist.append(circular_list[(start + offset) % n])
            if product_equals_247(sublist):
                result.append(sublist)
    return result