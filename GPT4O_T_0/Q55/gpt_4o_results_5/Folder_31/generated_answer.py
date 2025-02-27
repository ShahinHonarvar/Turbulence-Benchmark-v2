def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = []
            for i in range(end):
                sublist.append(circular_list[(start + i) % n])
            if product_of_list(sublist) == -16:
                result.append(sublist)
    return result