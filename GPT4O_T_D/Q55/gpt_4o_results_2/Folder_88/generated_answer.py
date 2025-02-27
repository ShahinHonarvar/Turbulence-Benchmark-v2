def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sub):
        product = 1
        for num in sub:
            product *= num
        return product
    n = len(circular_list)
    sublists = []
    for start in range(n):
        for length in range(1, n + 1):
            if start + length <= n:
                sublist = circular_list[start:start + length]
            else:
                sublist = circular_list[start:] + circular_list[:(start + length) % n]
            if product_of_sublist(sublist) == -56:
                sublists.append(sublist)
    return sublists