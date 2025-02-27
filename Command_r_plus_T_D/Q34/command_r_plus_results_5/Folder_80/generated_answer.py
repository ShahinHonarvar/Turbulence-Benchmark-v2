def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Function requires exactly 453 arguments.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    smallest_set = set()
    for s in args:
        if s.issubset(original_set) and len(s) < len(smallest_set) or not smallest_set:
            smallest_set = s
    return smallest_set