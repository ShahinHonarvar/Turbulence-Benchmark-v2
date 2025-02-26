def find_original_set(*sets):
    if len(sets) != 733:
        raise ValueError('Function must be called with exactly 733 distinct sets')
    original_set = set()
    for subset in sets:
        original_set.update(subset)
    return original_set