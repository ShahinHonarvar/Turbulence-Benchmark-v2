def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set()
    for s in args:
        original_set |= s
    return original_set