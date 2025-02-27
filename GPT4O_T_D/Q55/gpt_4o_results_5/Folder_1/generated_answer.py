def lists_with_product_equal_n(circular_list):

    def get_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(end)]
            if get_product(sublist) == -51:
                result.append(sublist)
    return result