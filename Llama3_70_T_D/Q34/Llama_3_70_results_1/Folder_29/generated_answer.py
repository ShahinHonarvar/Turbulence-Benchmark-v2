def find_original_set(*args):
    if len(args) != 94:
        raise TypeError('Exactly 94 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not all((isinstance(i, int) for i in arg)):
            raise TypeError('All elements of the sets must be integers')
        original_set.update(arg)
    return original_set