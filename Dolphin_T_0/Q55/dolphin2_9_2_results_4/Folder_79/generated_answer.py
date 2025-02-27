def lists_with_product_equal_n(lst):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    def circular_shift(lst, shift):
        len_lst = len(lst)
        return lst[shift:] + lst[:shift]
    len_lst = len(lst)
    result = []
    for shift in range(len_lst):
        circular_tuple = tuple(circular_shift(lst, shift))
        if not any([product(lst[i:i + len_shift]) != -83 for i in range(len_shift)]):
            result.append(list(circular_tuple))
    result = [list(x) for x in set((tuple(x) for x in result))]
    return result