def find_original_set(*args):
    if len(args) != 714:
        raise TypeError('find_original_set expected 714 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set = original_set.union(arg)
    return original_set