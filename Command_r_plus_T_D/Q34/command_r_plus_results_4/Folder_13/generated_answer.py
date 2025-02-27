def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Exactly 845 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    for s in args:
        if not original_set.issuperset(s):
            raise ValueError('The sets are not mutually comparable.')
    return original_set