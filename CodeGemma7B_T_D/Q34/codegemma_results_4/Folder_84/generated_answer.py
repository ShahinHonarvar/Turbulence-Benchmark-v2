def find_original_set(*args):
    min_set = min(args, key=len)
    for s in args:
        if not s <= min_set:
            return None
    return min_set