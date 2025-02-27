def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start_index in range(n):
        for length in range(1, n + 1):
            sublist = [circular_list[(start_index + i) % n] for i in range(length)]
            if product(sublist) == 91:
                result.append(sublist)
    return result