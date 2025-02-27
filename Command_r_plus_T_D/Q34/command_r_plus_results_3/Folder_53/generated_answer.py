def find_original_set(*args):
    if len(args) != 84:
        raise ValueError('Exactly 84 arguments are required.')
    if not all((isinstance(s, set) and s.issubset(set(range(1, 85))) for s in args)):
        raise ValueError('All arguments must be distinct sets of integers from 1 to 84.')
    original_set = set()
    for s in args:
        original_set = original_set.union(s)
    return original_set