def lists_with_product_equal_n(circular_list):

    def product_of_sublist(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    result = []
    n = len(circular_list)
    extended_list = circular_list * 2
    for start in range(n):
        for end in range(start, start + n):
            sublist = extended_list[start:end + 1]
            if product_of_sublist(sublist) == 13:
                result.append(sublist)
    return result