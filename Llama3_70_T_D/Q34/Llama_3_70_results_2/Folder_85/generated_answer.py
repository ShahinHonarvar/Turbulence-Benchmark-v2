def find_original_set(*args):
    if len(args) != 85:
        raise TypeError('find_original_set expected 85 arguments, got {}'.format(len(args)))
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments to find_original_set must be sets')
        if not s.issubset(original_set):
            original_set = original_set.union(s)
    return original_set