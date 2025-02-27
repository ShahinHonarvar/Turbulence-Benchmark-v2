def find_original_set(*args):
    min_set = set(args[0])
    for s in args[1:]:
        min_set &= s
    return min_set