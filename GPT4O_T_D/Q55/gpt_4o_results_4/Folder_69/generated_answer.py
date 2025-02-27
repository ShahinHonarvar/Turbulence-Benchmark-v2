def lists_with_product_equal_n(circular_list):

    def product_of_sublist(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = []
            for i in range(size):
                index = (start + i) % n
                sublist.append(circular_list[index])
            if product_of_sublist(sublist) == 90:
                result.append(sublist)
    return result