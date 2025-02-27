def find_original_set(*args):
    if len(set(args)) != 80:
        raise ValueError('The function requires 80 distinct sets as arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set