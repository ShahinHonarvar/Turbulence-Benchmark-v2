def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circular_list)
    circular_list += circular_list
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end]
            if product_of_list(sublist) == 51:
                result.append(sublist)
    return result