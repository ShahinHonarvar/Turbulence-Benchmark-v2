def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    for start in range(n):
        for length in range(1, n + 1):
            sublist = []
            for i in range(length):
                sublist.append(circular_list[(start + i) % n])
            if product_of_sublist(sublist) == 28:
                result.append(sublist)
    return result