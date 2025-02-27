def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            current_sublist = [circular_list[(i + k) % n] for k in range(j)]
            if product(current_sublist) == -41:
                result.append(current_sublist)
    return result