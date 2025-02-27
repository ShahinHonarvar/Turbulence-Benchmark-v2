def find_original_set(*args):
    universal_set = set()
    for arg in args:
        universal_set.update(arg)
    return universal_set