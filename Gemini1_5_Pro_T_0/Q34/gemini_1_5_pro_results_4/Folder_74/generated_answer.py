def find_original_set(*args):
    if len(set(args)) != 96:
        raise ValueError('The function must take exactly 96 distinct sets as arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set