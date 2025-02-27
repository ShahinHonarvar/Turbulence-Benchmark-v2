from itertools import islice, cycle, combinations

def lists_with_product_equal_n(lst):

    def circular_slice(lst, start, length):
        return islice(cycle(lst), start, start + length)

    def product(iterable):
        return reduce(lambda x, y: x * y, iterable, 1)

    def filter_sublists(lst):
        return [sublist for sublist in combinations(lst, len(lst) - 1) if product(sublist) == n]
    n = 28
    return [list(s) for s in filter_sublists(circular_slice(lst, i, len(lst) - 1)) for i in range(len(lst))]