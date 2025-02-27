def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    if not all((len(s) == len(set(s)) for s in args)):
        raise ValueError('All arguments must be distinct sets.')
    original_set = set.union(*args)
    return original_set