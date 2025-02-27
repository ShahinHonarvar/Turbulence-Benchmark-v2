def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                sublist.append(circular_list[(start + i) % n])
                if product(sublist) == -54:
                    result.append(sublist[:])
    return result