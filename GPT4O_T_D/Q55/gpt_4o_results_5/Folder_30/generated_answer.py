def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start_index in range(n):
        for sublist_size in range(1, n + 1):
            sublist = [circular_list[(start_index + i) % n] for i in range(sublist_size)]
            if product_of_sublist(sublist) == 99:
                result.append(sublist)
    return result