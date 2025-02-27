def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Function takes exactly 37 arguments')
    for arg in args:
        if not all((isinstance(i, int) for i in arg)):
            raise TypeError('All elements in the sets must be integers')
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must be sets, not lists or tuples')
    return set.union(*args)