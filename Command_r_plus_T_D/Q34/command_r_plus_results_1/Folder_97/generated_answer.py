def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    for s in args:
        if not s.issubset(original_set):
            raise ValueError('All arguments must be subsets of the original set.')
    return original_set