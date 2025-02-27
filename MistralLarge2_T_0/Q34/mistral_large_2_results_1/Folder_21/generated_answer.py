def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 arguments are required.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set