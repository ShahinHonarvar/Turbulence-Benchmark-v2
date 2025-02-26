def find_original_set(*sets):
    merged = set()
    for s in sets:
        merged.update(s)
    return sorted(merged)