def find_original_set(*args):
    min_set = set(range(1, 278))
    for s in args:
        min_set &= s
    return min_set