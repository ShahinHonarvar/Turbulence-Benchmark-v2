def find_original_set(*args):
    if len(args) != 851:
        raise ValueError('Exactly 851 sets must be provided')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set