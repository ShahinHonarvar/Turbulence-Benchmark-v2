def find_original_set(set1, set2, *args):
    union = set1 | set2
    for s in args:
        union |= s
    return union