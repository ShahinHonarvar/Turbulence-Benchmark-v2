def find_original_set(*args):
    if len(args) != 78:
        return 'Invalid number of arguments'
    s = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            return 'Invalid argument'
        s = s.union(arg)
    return s