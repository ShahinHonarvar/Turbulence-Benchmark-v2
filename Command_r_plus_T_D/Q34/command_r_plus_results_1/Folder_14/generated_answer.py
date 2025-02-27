def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('Exactly 13 arguments are required.')
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in args)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set.union(*args)
    for s in args:
        if not s.issubset(original_set):
            raise ValueError('The original set must contain all elements from the given sets.')
    return original_set