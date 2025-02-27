def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Expected 990 arguments, got {}'.format(len(args)))
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        result.update(arg)
    return result