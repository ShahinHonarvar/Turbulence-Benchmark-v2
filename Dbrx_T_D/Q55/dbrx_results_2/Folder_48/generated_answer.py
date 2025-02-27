from itertools import islice, cycle

def window(iterable, size):
    """Return a sliding window of size 'size' over 'iterable'."""
    it = iter(iterable)
    result = list(islice(it, size))
    if len(result) == size:
        yield result
    for elem in it:
        result = result[1:] + [elem]
        yield result

def multiple_of_990(n, L):
    """Return True if there is a sublist in 'L' that multiplied gives 'n'."""
    for i in range(1, len(L) + 1):
        if n % 1 == 0 and n == sublists_product(L, i):
            return True
    return False

def sublists_product(L, size):
    """Return the product of the elements in each sublist of size 'size' in 'L'."""
    return [sublist_product(sublist) for sublist in window(L, size)]

def sublist_product(L):
    """Return the product of the elements in 'L'."""
    return reduce(lambda x, y: x * y, L, 1)

def lists_with_product_equal_n(L):
    """Return a list of sublists in 'L' that multiplied gives 990."""
    return [sublist for sublist in itertools.permutations(L, len(L)) if multiple_of_990(990, list(sublist))]