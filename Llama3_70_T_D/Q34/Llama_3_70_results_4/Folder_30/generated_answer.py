def find_original_set(*args):
    if len(args) != 78:
        raise TypeError('find_original_set() takes exactly 78 arguments')
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(x, int) for x in arg)):
            raise TypeError('All arguments must be sets of integers')
    return set.union(*args)