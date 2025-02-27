def find_original_set(*sets):
    result = min(sets, key=len)
    for s in sets:
        if not s.issubset(result):
            return find_original_set(*(set(result).union(s) for s in sets))
    return result