def find_original_set(*sets):
    if len(sets) != 88:
        raise ValueError('This function takes exactly 88 distinct arguments.')
    super_set = set()
    for s in sets:
        if isinstance(s, set):
            super_set = super_set.union(s)
        else:
            raise ValueError('All arguments must be sets.')
    return super_set