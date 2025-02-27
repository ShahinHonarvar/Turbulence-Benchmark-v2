from itertools import combinations

def lists_with_product_equal_n(lst):

    def circular_sublists(lst):
        return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    sublists = circular_sublists(lst)
    result = [sublist for sublist in sublists if product(sublist) == -32]
    return result