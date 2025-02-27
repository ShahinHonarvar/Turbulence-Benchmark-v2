from itertools import islice, cycle

def window(iterable, size):
    """Returns a sliding window of size 'size' over 'iterable'."""
    it = iter(iterable)
    result = tuple(islice(it, size))
    if len(result) == size:
        yield result
    for element in it:
        result = result[1:] + (element,)
        yield result

def lists_with_product_equal_n(circular_list, n=43):
    """Returns a list of sublists each of which contains the contiguous integers from the given circular list such that their product equals 'n'."""
    sublists = []
    circular_list = list(circular_list)
    for i in range(len(circular_list)):
        for sublist in window(circular_list[i:] + circular_list[:i], len(circular_list)):
            if n in (prod := set(map(frozenset, itertools.product(*sublist)))):
                sublists.append(list(map(tuple, itertools.islice(iter(prod.difference(n)), len(sublist)))))
    return sublists