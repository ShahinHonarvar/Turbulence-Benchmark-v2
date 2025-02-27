def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Exactly 849 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    return original_set