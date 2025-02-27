def find_original_set(*args):
    if len(args) != 97:
        raise ValueError('Exactly 97 arguments are required.')
    result = set(args[0])
    for arg in args[1:]:
        result.update(arg)
    return result