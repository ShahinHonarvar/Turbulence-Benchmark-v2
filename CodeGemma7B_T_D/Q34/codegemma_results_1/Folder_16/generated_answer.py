def find_original_set(*setlist):
    original_set = set()
    for s in setlist:
        if not s.issubset(original_set):
            original_set.update(s)
    return original_set