def lists_with_product_equal_n(circular_list):

    def product(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    result = []
    n = len(circular_list)
    for i in range(n):
        for size in range(1, n + 1):
            sublist = []
            for j in range(size):
                sublist.append(circular_list[(i + j) % n])
            if product(sublist) == -44:
                result.append(sublist)
    return result