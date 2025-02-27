def find_original_set(*args):
    original_set = set()
    for arg in args:
        original_set.update(arg)
    for arg in args:
        if not arg.issubset(original_set):
            return None
    return original_set