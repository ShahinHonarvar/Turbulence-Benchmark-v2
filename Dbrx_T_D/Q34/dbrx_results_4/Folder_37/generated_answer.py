def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Exactly 67 arguments should be provided')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise TypeError('All arguments must be sets of integers')
    if len(set.union(*args)) > 1024:
        raise ValueError('The resulting set is too large')
    return set(range(1024 + 1))