def lists_with_product_equal_n(circular_list):

    def valid_product(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > 29:
                return False
        return product == 29
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                sublist.append(circular_list[(start + i) % n])
            if valid_product(sublist):
                result.append(sublist)
    return result