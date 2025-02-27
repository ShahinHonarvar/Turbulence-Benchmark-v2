def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for number in lst:
            product *= number
        return product
    n = len(circular_list)
    result = []
    for i in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(i + j) % n] for j in range(length)]
            if product_of_list(sublist) == -17:
                result.append(sublist)
    return result