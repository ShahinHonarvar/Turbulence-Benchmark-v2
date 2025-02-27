def find_original_set(*sets):
    if len(sets) != 33:
        raise ValueError('Exactly 33 sets are required')
    union_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise TypeError('All arguments must be sets of integers')
        union_set |= s
    return union_set