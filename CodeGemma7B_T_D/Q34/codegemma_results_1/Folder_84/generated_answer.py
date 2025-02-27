def find_original_set(*sets):
    union = set()
    for s in sets:
        union |= s
    return min(sets, key=len)