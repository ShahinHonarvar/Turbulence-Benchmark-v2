def find_original_set(*args):
    if len(args) != 85:
        raise TypeError('Expected exactly 85 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set.update(arg)
    return original_set