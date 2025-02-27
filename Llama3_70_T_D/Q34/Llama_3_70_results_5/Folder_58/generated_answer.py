def find_original_set(*args):
    if len(args) != 733:
        raise TypeError('Expected 733 arguments')
    original_set = set()
    for s in args:
        if not isinstance(s, set) or not s.issubset(set(range(-2 ** 31, 2 ** 31))):
            raise TypeError('Each argument must be a set of integers')
        original_set |= s
    return original_set