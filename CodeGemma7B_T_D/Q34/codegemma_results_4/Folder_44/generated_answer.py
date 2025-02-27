def find_original_set(*args):
    original_set = min(args, key=len)
    return original_set