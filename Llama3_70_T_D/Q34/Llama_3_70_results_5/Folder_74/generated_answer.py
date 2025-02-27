def find_original_set(*args):
    if len(args) != 96:
        raise TypeError('Expected 96 arguments, got {}'.format(len(args)))
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        if not arg.issubset(set.union(*args)):
            raise ValueError('Not all sets are subsets of the union of all sets')
        original_set.update(arg)
    return original_set