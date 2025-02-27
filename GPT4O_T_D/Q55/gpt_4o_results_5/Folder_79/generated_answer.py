def lists_with_product_equal_n(circular_list):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = []
            for i in range(size):
                sublist.append(circular_list[(start + i) % n])
            if get_product(sublist) == -83:
                result.append(sublist)
    return result