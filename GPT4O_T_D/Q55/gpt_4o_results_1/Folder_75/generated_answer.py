def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    lst_length = len(circular_list)
    result = []
    for start in range(lst_length):
        for size in range(1, lst_length + 1):
            sublist = []
            for i in range(size):
                sublist.append(circular_list[(start + i) % lst_length])
            if product(sublist) == 13:
                result.append(sublist)
    return result