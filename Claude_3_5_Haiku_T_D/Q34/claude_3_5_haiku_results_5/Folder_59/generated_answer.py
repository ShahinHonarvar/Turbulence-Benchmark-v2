def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Function requires exactly 10 sets')
    if any((not isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets')
    if any((len(s) == 0 for s in args)):
        raise ValueError('All sets must be non-empty')
    return set().union(*args)