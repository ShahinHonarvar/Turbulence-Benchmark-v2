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
            if end <= n:
                sublist = circular_list[start:start + end]
                if product(sublist) == -20:
                    result.append(sublist)
            else:
                sublist = circular_list[start:] + circular_list[:end - n]
                if product(sublist) == -20:
                    result.append(sublist)
    return result