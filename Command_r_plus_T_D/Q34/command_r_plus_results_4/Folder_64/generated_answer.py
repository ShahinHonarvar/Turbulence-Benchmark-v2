def find_original_set(*args):
    if len(args) != 7 or len(set(args)) != 7:
        raise ValueError('Exactly 7 distinct sets are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set