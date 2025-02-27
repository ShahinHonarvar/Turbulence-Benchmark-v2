def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('Exactly 132 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    if not all((len(s) == len(set(s)) for s in args)):
        raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set