def find_original_set(*args):
    union_set = set().union(*args)
    for i in range(1, len(union_set) + 1):
        for subset in itertools.combinations(union_set, i):
            if all((s.issubset(subset) for s in args)):
                return set(subset)
    return set()