from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def circular_sublists(lst, n):
        return [lst[i:i + n] for i in range(len(lst) - n + 1)]

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return [sl for sl in circular_sublists(lst, len(lst)) if product(sl) == 48]