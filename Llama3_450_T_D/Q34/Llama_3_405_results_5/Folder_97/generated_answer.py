def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((isinstance(x, int) for s in args for x in s)):
        raise ValueError('All set elements must be integers')
    return set.union(*args)