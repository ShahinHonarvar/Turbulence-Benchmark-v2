def find_original_set(*args):
    if len(args) != 16:
        raise ValueError('Exactly 16 arguments are required.')
    if any((not isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if any((not all((isinstance(item, int) for item in arg)) for arg in args)):
        raise TypeError('All items in the sets must be integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set