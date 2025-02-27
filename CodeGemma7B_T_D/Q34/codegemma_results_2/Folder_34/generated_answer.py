def find_original_set(*args):
    min_set = min(args, key=len)
    for s in args:
        if s not in [min_set]:
            min_set.update(s)
    return min_set