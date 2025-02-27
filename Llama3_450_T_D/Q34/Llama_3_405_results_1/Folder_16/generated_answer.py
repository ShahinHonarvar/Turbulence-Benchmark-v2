def find_original_set(*args):
    if len(args) != 321 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Exactly 321 distinct sets are required')
    original_set = set()
    for arg in args:
        original_set = original_set.union(arg)
    return original_set