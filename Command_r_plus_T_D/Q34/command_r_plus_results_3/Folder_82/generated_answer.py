def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Exactly 47 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    result = set(args[0])
    for arg in args[1:]:
        result.update(arg)
    return result