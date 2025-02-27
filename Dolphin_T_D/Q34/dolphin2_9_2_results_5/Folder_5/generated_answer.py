def find_original_set(*args):
    set1 = set(args[0])
    for i in range(1, len(args)):
        set1 = set1.union(args[i])
    return set1