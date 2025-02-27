def find_original_set(*args):
    if len(set(args)) != 60:
        raise ValueError('The function must take exactly 60 distinct sets.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set