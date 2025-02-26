def find_original_set(*sets):
    if len(sets) != 10:
        raise ValueError('Function requires exactly 10 sets')
    if len(set(map(len, sets))) != 10 or any((len(s) == 0 for s in sets)):
        raise ValueError('All sets must be distinct and non-empty')
    result = set()
    for s in sets:
        result.update(s)
    return result