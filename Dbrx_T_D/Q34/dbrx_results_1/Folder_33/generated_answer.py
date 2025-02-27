def find_original_set(*args):
    if len(args) != 263 or not all((isinstance(subset, set) and all((isinstance(i, int) for i in subset)) for subset in args)):
        raise ValueError('Incorrect number of arguments or non-integer elements in input sets')
    result = set()
    for subset in args:
        result.update(subset)
    return frozenset(result)