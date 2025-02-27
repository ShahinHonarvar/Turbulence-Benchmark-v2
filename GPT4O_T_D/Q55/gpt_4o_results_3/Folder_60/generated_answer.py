def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for i in range(n):
        for length in range(1, n + 1):
            sublist = []
            for j in range(length):
                index = (i + j) % n
                sublist.append(circular_list[index])
            if product_of_list(sublist) == 49:
                result.append(sublist)
    return result