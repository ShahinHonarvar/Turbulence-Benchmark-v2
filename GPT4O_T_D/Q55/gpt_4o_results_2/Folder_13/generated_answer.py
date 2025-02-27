def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    extended_list = circular_list * 2
    for i in range(n):
        for length in range(1, n + 1):
            sublist = extended_list[i:i + length]
            if product_of_list(sublist) == 54:
                result.append(sublist)
    return result