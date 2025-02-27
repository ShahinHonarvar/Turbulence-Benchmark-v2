def find_original_set(*args):
    min_set = set()
    for arg in args:
        min_set.update(arg)
    return min_set