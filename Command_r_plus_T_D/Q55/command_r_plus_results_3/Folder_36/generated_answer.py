def lists_with_product_equal_n(circular_list):

    def product_equal_n(lst, n):
        product = 1
        for num in lst:
            product *= num
        return product == n
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if product_equal_n(sublist, 714):
                result.append(sublist)
    return result