def find_original_set(*args):
    if len(args) != 790:
        raise TypeError('find_original_set() takes exactly 790 arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(x, int) for x in arg)):
            raise TypeError('All elements of the sets must be integers')
        original_set.update(arg)
    return original_set