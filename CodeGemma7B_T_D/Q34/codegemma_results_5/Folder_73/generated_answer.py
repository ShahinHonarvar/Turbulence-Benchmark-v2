def find_original_set(*args):
    if len(args) != 19 or len({frozenset(s) for s in args}) != 19:
        raise ValueError('Invalid input.')
    result = set()
    for s in args:
        result |= s
    return result