def find_original_set(*args):
    if len(args) != 537:
        raise TypeError('find_original_set expected 537 arguments, got {}'.format(len(args)))
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    if not all((isinstance(item, int) for arg in args for item in arg)):
        raise TypeError('All items in the sets must be integers')
    return set.union(*args)