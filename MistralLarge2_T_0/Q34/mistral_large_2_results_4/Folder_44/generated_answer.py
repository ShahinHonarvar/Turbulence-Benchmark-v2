def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Exactly 926 arguments are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set