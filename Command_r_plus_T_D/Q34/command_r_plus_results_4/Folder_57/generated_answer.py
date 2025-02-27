def find_original_set(*args):
    if len(args) != 93:
        raise ValueError('Function requires exactly 93 arguments')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets')
    original_set = set.union(*args)
    for arg in args:
        if not original_set.issuperset(arg):
            raise ValueError('Arguments are not all subsets of the original set')
    return original_set