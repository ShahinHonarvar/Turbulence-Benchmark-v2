def find_original_set(*args):
    s = set()
    for i in range(51):
        s = s.union(args[i])
    return s