def find_original_set(*args):
    if args == {}:
        return set()
    return reduce(union_sets, args)

def union_sets(set1, set2):
    return set1.union(set2)