def find_original_set(*args):
    if len(args) != 828:
        raise TypeError('Expected 828 arguments, got {}'.format(len(args)))
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
    return set.union(*args)