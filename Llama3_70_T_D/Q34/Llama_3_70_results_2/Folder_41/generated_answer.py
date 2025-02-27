def find_original_set(*args):
    if len(args) != 20:
        raise TypeError('Exactly 20 distinct arguments are required')
    if len(set(map(frozenset, args))) != 20:
        raise TypeError('All 20 arguments must be distinct')
    if not all((isinstance(arg, set) and arg.issubset(range(-2 ** 31, 2 ** 31)) for arg in args)):
        raise TypeError('All arguments must be sets of integers')
    result = set()
    for s in args:
        result.update(s)
    return result