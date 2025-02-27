def find_original_set(*args):
    if len(args) != 43:
        raise TypeError('find_original_set expected 43 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise TypeError('All arguments must be sets of integers.')
        original_set = original_set.union(arg)
    return original_set