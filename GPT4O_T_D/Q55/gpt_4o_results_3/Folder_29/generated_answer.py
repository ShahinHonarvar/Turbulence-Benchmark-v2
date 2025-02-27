def lists_with_product_equal_n(circular_list):

    def product_of_sublists(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            sublist = []
            for index in range(start, start + size):
                sublist.append(circular_list[index % n])
            if product_of_sublists(sublist) == 15:
                result.append(sublist)
    return result