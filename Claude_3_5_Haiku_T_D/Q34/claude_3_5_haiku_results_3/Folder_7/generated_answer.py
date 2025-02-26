def find_original_set(*sets):
    if len(sets) != 537:
        raise ValueError('Function must be called with exactly 537 sets')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set