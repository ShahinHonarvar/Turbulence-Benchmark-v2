def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            sublist = []
            for i in range(end):
                sublist.append(circular_list[(start + i) % n])
            if product(sublist) == -81:
                result.append(sublist)
    return result