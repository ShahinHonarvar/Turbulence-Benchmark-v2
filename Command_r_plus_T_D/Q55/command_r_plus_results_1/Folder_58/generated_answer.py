def lists_with_product_equal_n(circular_list):

    def product_equal_n(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1 + i):
            sublist = circular_list[i:j] % len(circular_list)
            if product_equal_n(sublist) == 733:
                result.append(sublist)
    return result