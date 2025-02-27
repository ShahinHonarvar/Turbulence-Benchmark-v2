def find_original_set(*args):
    original_set = set()
    for argument_set in args:
        original_set = original_set.union(argument_set)
    return original_set