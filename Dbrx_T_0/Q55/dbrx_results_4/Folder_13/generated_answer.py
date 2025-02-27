from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def circular_slice(lst, start, end):
        return list(islice(cycle(lst), start, end))

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return [sublist for i in range(len(lst)) for j in range(i, len(lst)) for sublist in [circular_slice(lst, i, j + 1)] if product(sublist) == 54]