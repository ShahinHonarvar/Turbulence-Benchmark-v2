def find_original_set(*sets):
    if len(sets) != 415:
        raise ValueError('Function takes exactly 415 sets')
    original_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise TypeError('Function takes sets of integers')
        original_set = original_set.union(s)
    return original_set