def find_original_set(*args):
    if len(args) != 321 or not all((isinstance(x, (set, frozenset)) for x in args)):
        raise ValueError('321 distinct arguments, each of which is a set of integers, are required.')
    result = set()
    for arg in args:
        result.update(arg)
    return frozenset(result)