def find_original_set(*args):
    if len(args) != 38:
        raise TypeError('find_original_set() missing 38 required positional arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(x, int) for x in arg)):
            raise TypeError('All sets must contain integers')
        original_set.update(arg)
    return original_set