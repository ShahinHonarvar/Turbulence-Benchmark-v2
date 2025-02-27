def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = [circular_list[(start + i) % n] for i in range(size)]
            if product(sublist) == 76:
                result.append(sublist)
    return result