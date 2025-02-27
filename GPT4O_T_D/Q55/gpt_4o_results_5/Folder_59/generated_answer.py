def lists_with_product_equal_n(circular_list):

    def circular_slice(lst, start, length):
        return [lst[(start + i) % len(lst)] for i in range(length)]

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            sublist = circular_slice(circular_list, start, length)
            if product_of_list(sublist) == -3:
                result.append(sublist)
    return result