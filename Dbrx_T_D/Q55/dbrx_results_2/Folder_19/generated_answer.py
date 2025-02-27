from itertools import islice, cycle

def lists_with_product_equal_n(lst, n=-54):

    def circular_slice(it, start, stop):
        return islice(cycle(it), start, stop) if start < stop else islice(cycle(it), start, None) | islice(cycle(it), 0, stop)

    def sublist_from_circular_slice(subslice, start):
        return [subslice + (lst[idx] if idx < len(lst) else 0) for idx in range(start, start + len(subslice))]

    def product(lst):
        return reduce(lambda x, y: x * y, lst, 1)
    return [sublist for sublist in (list(sublist_from_circular_slice(subslice, start)) for start in range(len(lst)) for subslice in (s for s in circular_slice(lst, start, stop) if s != [])) if product(sublist) == n]