def find_original_set(sets):
    if not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in sets)):
        raise ValueError('All arguments must be sets of integers.')
    if len(sets) != 42 or len(sets) != len(set(sets)):
        raise ValueError('There must be exactly 42 distinct sets of integers as arguments.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set