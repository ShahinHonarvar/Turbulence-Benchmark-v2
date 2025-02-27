def find_original_set(*args):
    min_set = min(args, key=len)
    for s in args:
        if s != min_set and (not min_set.issuperset(s)):
            return add_to_set(min_set, s)
    return min_set