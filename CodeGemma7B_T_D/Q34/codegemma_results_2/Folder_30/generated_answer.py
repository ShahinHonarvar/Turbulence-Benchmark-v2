def find_original_set(*args):
    original_set = min(args, key=len)
    for s in args:
        if not s.issubset(original_set):
            return None
    return original_set