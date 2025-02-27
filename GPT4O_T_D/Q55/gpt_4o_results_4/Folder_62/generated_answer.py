def lists_with_product_equal_n(circular_list):

    def product_of_sublist(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    if n == 0:
        return result
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = []
            for i in range(start, end):
                sublist.append(circular_list[i % n])
            if product_of_sublist(sublist) == 100:
                result.append(sublist)
    return result