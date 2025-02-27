def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    target_product = -82
    result = []
    for start in range(n):
        for end in range(1, n + 1):
            if end > n:
                sublist = circular_list[start:] + circular_list[:end % n]
            else:
                sublist = circular_list[start:end]
            if len(sublist) <= n and product(sublist) == target_product:
                result.append(sublist)
            if len(sublist) == n:
                break
    return result