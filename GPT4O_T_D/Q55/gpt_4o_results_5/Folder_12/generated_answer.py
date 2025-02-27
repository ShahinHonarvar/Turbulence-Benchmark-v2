def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    list_extended = circular_list + circular_list
    results = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = list_extended[start:end]
            if product(sublist) == -18:
                if len(sublist) <= n:
                    results.append(sublist)
    return results