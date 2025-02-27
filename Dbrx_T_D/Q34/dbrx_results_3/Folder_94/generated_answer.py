def find_original_set(*args):
    if len(args) != 69:
        raise ValueError('Function takes exactly 69 arguments')
    if not all((isinstance(x, set) for x in args)):
        raise ValueError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise ValueError('All elements of sets must be integers')
    return set.union(*args)