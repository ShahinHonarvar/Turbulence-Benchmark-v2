def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if product_of_sublist(sublist) == -69:
                result.append(sublist)
    return result