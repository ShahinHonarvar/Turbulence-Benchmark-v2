def find_original_set(*args):
    if len(args) != 126:
        raise TypeError('find_original_set expected 126 arguments, got {}'.format(len(args)))
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('all arguments must be sets')
        original_set.update(s)
    return original_set