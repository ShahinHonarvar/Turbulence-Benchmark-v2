def find_original_set(*args):
    min_set = set()
    for s in args:
        min_set |= s
    if len(min_set) == 97:
        return min_set