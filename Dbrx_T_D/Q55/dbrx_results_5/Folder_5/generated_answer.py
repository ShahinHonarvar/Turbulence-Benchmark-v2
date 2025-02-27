from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists(lst):
        for i in range(1, len(lst) + 1):
            for j in islice(cycle(lst), i):
                yield j

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p

    def circular_sublists(lst):
        for i in range(len(lst)):
            yield (lst[i:] + lst[:i])
    return [sl for sl in circular_sublists(lst) if product(sl) == -33]