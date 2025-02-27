def find_original_set(*sets):
    original_set = set()
    for arg_set in sets:
        original_set.update(arg_set)
    return original_set