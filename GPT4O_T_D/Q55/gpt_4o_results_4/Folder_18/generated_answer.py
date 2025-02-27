def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            sublist = []
            for k in range(j):
                sublist.append(circular_list[(i + k) % n])
            if product(sublist) == 36:
                result.append(sublist)
    return result