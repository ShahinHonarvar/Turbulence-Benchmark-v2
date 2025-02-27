from itertools import islice, cycle, tee

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def mul_sublists(ln):
    return [list(x) for x in (sublist for sublist in sublists(ln) if sum((x > 0 for x in sublist)) > 0 and prod(sublist) == 415)]

def sublists(lst):
    for i in range(len(lst)):
        yield from pairwise(islice(cycle(lst), i, None))

def prod(lst):
    p = 1
    for x in lst:
        p *= x
    return p

def lists_with_product_equal_n(lst):
    return mul_sublists(lst)