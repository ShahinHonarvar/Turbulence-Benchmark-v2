def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(end)]
            if product_of_list(sublist) == -33:
                result.append(sublist)
    return result