from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def sublists(lst):
        for i in range(1, len(lst) + 1):
            for j in islice(cycle(range(len(lst))), i):
                yield (lst[j], lst[j - 1])

    def product(sublst):
        return reduce(lambda x, y: x * y, sublst, 1)
    return [list(sublst) for sublst in sublists(lst) if product(sublst) == 76]