def find_original_set(*args):
    if len(args) != 8 or not all((isinstance(arg, set) for arg in args)):
        raise ValueError('Exactly 8 distinct sets are required')
    original_set = set()
    for s in args:
        original_set.update(s)
    return original_set