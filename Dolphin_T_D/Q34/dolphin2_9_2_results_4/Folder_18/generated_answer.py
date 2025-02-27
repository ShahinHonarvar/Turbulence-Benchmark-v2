def find_original_set(*sets):
    if not all((isinstance(s, set) and s.issubset(s) and (len(s) < 1000) and s.isdisjoint(sets) for s in sets)):
        raise ValueError('Invalid input')
    result = set()
    for s in sets:
        result = result.union(s)
    return result