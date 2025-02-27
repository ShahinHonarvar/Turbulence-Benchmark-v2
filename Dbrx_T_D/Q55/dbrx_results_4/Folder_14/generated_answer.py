from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-72):

    def sublists(lst):
        for i in range(len(lst)):
            for j in range(i, len(lst)):
                yield lst[i:j + 1]

    def circular_sublists(lst):
        for sublist in sublists(lst):
            yield from (list(islice(cycle(sublist), i, len(sublist) + i)) for i in range(len(sublist)))
    return [sublist for sublist in circular_sublists(lst) if isinstance(sublist, int) or reduce(lambda x, y: x * y, sublist) == n]