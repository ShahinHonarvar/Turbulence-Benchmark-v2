def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Exactly 64 arguments are required.')
    if not all((isinstance(s, set) for s in args)):
        raise TypeError('All arguments must be sets.')
    if not all((all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All elements in the sets must be integers.')
    if not all((len(s) == len(set(s)) for s in args)):
        raise ValueError('All sets must contain distinct elements.')
    original_set = set.union(*args)
    for s in args:
        if not original_set.issuperset(s):
            raise ValueError('The arguments are not all subsets of the original set.')
    return original_set