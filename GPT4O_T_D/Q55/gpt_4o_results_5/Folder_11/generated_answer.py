def lists_with_product_equal_n(circular_list):

    def product(seq):
        result = 1
        for num in seq:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if product(sublist) == -15:
                result.append(sublist)
    return result