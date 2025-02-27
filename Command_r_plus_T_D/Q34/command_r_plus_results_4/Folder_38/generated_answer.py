def find_original_set(*args):
    unique_set = set().union(*args)
    for arg in args:
        unique_set = unique_set.intersection(arg)
    return unique_set