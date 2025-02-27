def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 arguments are required')
    if not all((isinstance(arg, set) and arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise ValueError('All arguments must be sets of integers')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All arguments must be distinct')
    if len(set((tuple(sorted(arg)) for arg in args))) != 87:
        raise ValueError('All arguments must be distinct')
    return set.union(*args)