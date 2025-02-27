from itertools import islice

def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        return [lst[i:i + j] for i in range(len(lst)) for j in range(1, len(lst) - i + 1)]

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)

    def valid_sublists(lst, n):
        return [sublst for sublst in lst if product(sublst) == n]
    return valid_sublists(circular_sublists(lst), 247)