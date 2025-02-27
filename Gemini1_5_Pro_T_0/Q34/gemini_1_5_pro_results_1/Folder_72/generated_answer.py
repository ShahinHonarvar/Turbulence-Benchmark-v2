def find_original_set(*args):
    if len(set(args)) != 87:
        raise ValueError('The function must take exactly 87 distinct arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set