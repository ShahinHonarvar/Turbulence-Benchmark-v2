def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Exactly 38 arguments are required')
    if len(set((id(arg) for arg in args))) != 38:
        raise ValueError('All arguments must be distinct sets')
    if not all((isinstance(arg, set) and arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    return set.union(*args)