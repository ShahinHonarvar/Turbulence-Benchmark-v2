def find_original_set(*args):
    if len(set(args)) != 100:
        raise ValueError('The function must take 100 distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set