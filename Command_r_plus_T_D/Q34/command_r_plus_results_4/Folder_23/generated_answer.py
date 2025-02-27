def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Function requires exactly 41 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    original_set = set.union(*args)
    for arg in args:
        if not original_set.issuperset(arg):
            raise ValueError('Arguments must be distinct sets')
    return original_set