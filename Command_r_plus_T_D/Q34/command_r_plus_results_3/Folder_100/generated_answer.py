def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('Exactly 91 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    result_set = set(args[0])
    for arg in args[1:]:
        result_set.update(arg)
    return result_set