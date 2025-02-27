def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Exactly 459 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets.')
    if not all((all((isinstance(x, int) for x in arg)) for arg in args)):
        raise ValueError('All set elements must be integers.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set