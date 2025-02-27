def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Invalid number of arguments')
    min_set = set()
    for s in args:
        if not s.issubset(min_set):
            min_set = s
    return min_set