def find_original_set(*sets):
    if len(sets) != 24:
        raise ValueError('Exactly 24 sets must be provided')
    for s in sets:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets')
        if not all((isinstance(x, int) for x in s)):
            raise ValueError('All sets must contain only integers')
    original_set = set()
    for s in sets:
        original_set |= s
    return original_set