def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    result = []
    n = len(circular_list)
    for start in range(n):
        for end in range(1, n + 1):
            sublist = []
            for index in range(start, start + end):
                sublist.append(circular_list[index % n])
            if product_of_list(sublist) == -20:
                result.append(sublist)
    return result