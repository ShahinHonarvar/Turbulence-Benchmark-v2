def find_original_set(*args):
    original_set = set()
    for i in args:
        if i not in original_set:
            original_set = original_set.union(i)
    return original_set