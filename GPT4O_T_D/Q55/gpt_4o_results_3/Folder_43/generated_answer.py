def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result_list = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = []
            for i in range(start, end):
                sublist.append(circular_list[i % n])
            if len(sublist) <= n and product(sublist) == -26:
                result_list.append(sublist)
    return result_list