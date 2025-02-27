def lists_with_product_equal_n(circular_list):

    def product_is_18(sublist):
        product = 1
        for number in sublist:
            product *= number
        return product == 18
    result = []
    n = len(circular_list)
    for i in range(n):
        for j in range(1, n + 1):
            sublist = [circular_list[(i + k) % n] for k in range(j)]
            if product_is_18(sublist):
                result.append(sublist)
    return result