def find_original_set(*args):
    if len(args) != 410:
        raise TypeError('find_original_set() takes exactly 410 arguments')
    if not all((isinstance(arg, set) and isinstance(x, int) for arg in args for x in arg)):
        raise TypeError('All arguments must be sets of integers')
    if not len(set((frozenset(arg) for arg in args))) == 410:
        raise TypeError('All arguments must be distinct')
    return set.union(*args)