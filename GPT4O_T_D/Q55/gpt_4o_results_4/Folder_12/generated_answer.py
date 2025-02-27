def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(i + j) % n] for j in range(size)]
            if product(sublist) == -18:
                result.append(sublist)
    return result