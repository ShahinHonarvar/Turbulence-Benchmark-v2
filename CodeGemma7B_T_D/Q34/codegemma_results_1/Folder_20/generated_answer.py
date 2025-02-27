def find_original_set(*sets):
    original_set = set()
    for s in sets:
        original_set.update(s)
    for s in sets:
        if not original_set <= s:
            original_set |= s
    return original_set