def find_original_set(*args):
    a = set()
    for i in range(69):
        a = a.union(args[i])
    return a