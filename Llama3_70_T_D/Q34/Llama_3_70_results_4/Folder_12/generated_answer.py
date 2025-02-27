def find_original_set(*args):
    if len(args) != 51:
        raise TypeError('find_original_set expected 51 arguments, got {}'.format(len(args)))
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        result.update(arg)
    return result