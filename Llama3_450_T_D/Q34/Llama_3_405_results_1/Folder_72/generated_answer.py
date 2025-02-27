def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 arguments are required')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All arguments must be distinct sets')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All elements of the sets must be integers')
    return set.union(*args)