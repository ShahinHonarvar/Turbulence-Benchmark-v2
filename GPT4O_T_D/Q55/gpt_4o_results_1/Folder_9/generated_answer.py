def lists_with_product_equal_n(circular_list):

    def calculate_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = []
            for i in range(size):
                sublist.append(circular_list[(start + i) % n])
            if calculate_product(sublist) == -36:
                result.append(sublist)
    return result