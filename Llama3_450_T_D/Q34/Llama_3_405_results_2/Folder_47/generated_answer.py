def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 sets must be provided')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for s in args for x in s)):
        raise ValueError('All set elements must be integers')
    return set.union(*args)