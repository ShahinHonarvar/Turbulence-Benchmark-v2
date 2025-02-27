def find_original_set(*args):
    if len(args) != 91:
        return 'Invalid input'
    s = set()
    for a in args:
        if not isinstance(a, set) or not a.issubset(s):
            s = a
    return s