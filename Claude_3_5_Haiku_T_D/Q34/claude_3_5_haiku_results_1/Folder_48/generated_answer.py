def find_original_set(*sets_args):
    if len(sets_args) != 990:
        raise ValueError('Function must receive exactly 990 sets')
    original_set = set()
    for current_set in sets_args:
        original_set.update(current_set)
    return original_set