def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in arg)) for arg in args)):
        raise TypeError('All elements in sets must be integers.')
    if not all((len(arg) == len(set(arg)) for arg in args)):
        raise ValueError('All arguments must be distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set