def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    sublists = []
    for start in range(n):
        for size in range(1, n + 1):
            end = (start + size) % n
            if start < end:
                sublist = circular_list[start:end]
            else:
                sublist = circular_list[start:n] + circular_list[0:end]
            if product(sublist) == 13:
                sublists.append(sublist)
    return sublists