def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('Exactly 59 arguments required')
    original_set = set()
    for current_set in args:
        original_set.update(current_set)
    return original_set