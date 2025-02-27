def find_original_set(*args):
    *sets, target_set = args
    original_set = set()
    for _set in sets:
        original_set = original_set.union(_set)
    if target_set.issubset(original_set):
        return original_set
    else:
        return None