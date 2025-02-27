def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = [circular_list[i % n] for i in range(start, end)]
            if product_of_list(sublist) == -32:
                result.append(sublist)
    return result