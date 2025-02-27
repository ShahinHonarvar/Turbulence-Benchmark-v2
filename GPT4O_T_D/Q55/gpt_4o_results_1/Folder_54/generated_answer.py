def lists_with_product_equal_n(circular_list):

    def sublist_product(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    results = []
    for start in range(n):
        for size in range(1, n + 1):
            end = start + size
            if end <= n:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:] + circular_list[:end % n]
            if sublist_product(sublist) == -17:
                results.append(sublist)
    return results