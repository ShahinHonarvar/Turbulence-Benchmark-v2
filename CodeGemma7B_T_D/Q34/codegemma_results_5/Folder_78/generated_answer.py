def find_original_set(*args):
    min_set = min(args, key=len)
    for s in args:
        if s != min_set and s.issubset(min_set):
            min_set.update(s)
    return min_set