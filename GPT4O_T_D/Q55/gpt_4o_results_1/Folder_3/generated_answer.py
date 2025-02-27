def lists_with_product_equal_n(circular_list):

    def product_of_list(sublist):
        product = 1
        for x in sublist:
            product *= x
        return product
    n = len(circular_list)
    sublists = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if product_of_list(sublist) == -22:
                sublists.append(sublist)
    return sublists