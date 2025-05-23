def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Exactly 10 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        if not all((isinstance(item, int) for item in arg)):
            raise ValueError('All items in the sets must be integers.')
        original_set.update(arg)
    return original_set