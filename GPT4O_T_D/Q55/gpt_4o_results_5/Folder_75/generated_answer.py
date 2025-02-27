def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            if length <= n:
                sublist = [circular_list[(start + i) % n] for i in range(length)]
                if product_of_list(sublist) == 13:
                    result.append(sublist)
    return result