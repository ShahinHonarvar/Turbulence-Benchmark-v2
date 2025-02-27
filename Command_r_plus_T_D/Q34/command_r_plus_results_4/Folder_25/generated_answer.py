def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Function requires exactly 38 arguments')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in sets must be integers')
    original_set = set.union(*args)
    for s in args:
        if not original_set.issuperset(s):
            raise ValueError('Invalid input sets')
    return original_set