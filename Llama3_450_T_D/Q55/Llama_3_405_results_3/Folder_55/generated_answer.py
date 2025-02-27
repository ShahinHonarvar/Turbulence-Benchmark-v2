def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    result = []
    n = len(circular_list)
    for length in range(1, n + 1):
        for start in range(n):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if get_product(sublist) == -6:
                result.append(sublist)
    return result