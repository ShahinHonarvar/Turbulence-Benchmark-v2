def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    if not all((len(s) == len(set(s)) for s in args)):
        raise ValueError('All arguments must be distinct sets.')
    original_set = set.union(*args)
    for s in args:
        if not s.issubset(original_set):
            raise ValueError('The original set is not a superset of all arguments.')
    return original_set