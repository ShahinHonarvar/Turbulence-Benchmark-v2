def find_original_set(*args):
    if len(args) != 126:
        raise ValueError('Exactly 126 arguments are required.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in the sets must be integers.')
    if len(set((frozenset(s) for s in args))) != 126:
        raise ValueError('All arguments must be distinct sets.')
    original_set = set.union(*args)
    return original_set