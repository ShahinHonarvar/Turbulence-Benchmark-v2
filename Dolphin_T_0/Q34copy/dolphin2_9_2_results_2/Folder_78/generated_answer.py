def find_original_set(*args):
    returned_set = set()
    for arg in args:
        returned_set = returned_set.union(arg)
    return returned_set