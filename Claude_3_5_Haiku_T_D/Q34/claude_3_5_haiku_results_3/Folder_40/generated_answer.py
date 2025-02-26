def find_original_set(s):
    original_set = set()
    for subset in s:
        original_set.update(subset)
    return original_set