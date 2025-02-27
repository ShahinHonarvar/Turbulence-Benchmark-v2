def find_original_set(*args):
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        result.update(arg)
    return result