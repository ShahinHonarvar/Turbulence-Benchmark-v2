def find_original_set(x):
    original_set = set()
    for s in x:
        original_set |= s
    return original_set