def find_original_set(*args):
    if len(args) != 91 or len(set(args)) != 91:
        raise ValueError('Exactly 91 distinct sets must be provided as arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set