def find_original_set(*args):
    s = set()
    for argument in args:
        s = s.union(argument)
    return s