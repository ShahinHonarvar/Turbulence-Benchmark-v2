def find_original_set(*sets):
    if len(sets) != 91:
        raise ValueError('The function needs exactly 91 arguments.')
    smallest_set = min(sets, key=len)
    for s in sets:
        if s != smallest_set and (not smallest_set.issuperset(s)):
            raise ValueError('The given sets are not a superset of the smallest set.')
    return smallest_set