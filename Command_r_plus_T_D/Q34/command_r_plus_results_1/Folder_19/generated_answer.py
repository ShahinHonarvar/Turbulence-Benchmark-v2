def find_original_set(*args):
    if len(args) != 23:
        raise ValueError('Exactly 23 arguments are required.')
    if not all((isinstance(s, set) and s.issubset(set(range(1, 24))) for s in args)):
        raise ValueError('All arguments must be distinct sets of integers from 1 to 23.')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set