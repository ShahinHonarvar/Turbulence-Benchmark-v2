def find_original_set(*args):
    max_set = max(args, key=len)
    for s in args:
        if not max_set.issuperset(s):
            max_set.update(s)
    return max_set