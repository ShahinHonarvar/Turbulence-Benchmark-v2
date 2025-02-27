def find_original_set(s):
    original_set = set()
    for x in s:
        original_set.update(x)
    return original_set