def find_original_set(*args):
    if len(args) != 685:
        raise TypeError('Expected 685 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(i, int) for i in arg)):
            raise TypeError('All sets must contain only integers')
    return set.union(*args)