def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('The function must take exactly 478 arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set