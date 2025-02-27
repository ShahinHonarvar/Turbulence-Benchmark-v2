def find_original_set(*args):
    if len(args) != 48:
        raise ValueError('Expected 48 arguments, got {}'.format(len(args)))
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets')
        if not s.issubset(original_set):
            original_set = original_set.union(s)
    return original_set