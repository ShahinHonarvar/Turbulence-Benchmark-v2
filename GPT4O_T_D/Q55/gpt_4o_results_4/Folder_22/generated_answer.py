def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(length)]
            if get_product(sublist) == 4:
                results.append(sublist)
    return results