from itertools import islice, cycle

def circular_list_product(lst, start, length):
    total = 1
    for i in range(start, start + length):
        total *= lst[i]
    return total

def circular_sublists(lst):
    for i in range(len(lst)):
        yield from window(cycle(lst), len(lst), i)

def window(seq, n, start):
    """Returns a sliding window (of width n) over data from the sequence"""
    "   whose first element is the item at position 'start'"
    '   see: https://docs..org/3/library/itertools.html#itertools-recipes'
    it = iter(seq)
    result = tuple(islice(it, start, start + n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def lists_with_product_equal_n(lst, n):
    return [sl for sl in circular_sublists(lst) if circular_list_product(sl, 0, len(sl)) == n]