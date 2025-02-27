def find_original_set(*args):
    min_set = set()
    for s in args:
        min_set.update(s)
    return min_set