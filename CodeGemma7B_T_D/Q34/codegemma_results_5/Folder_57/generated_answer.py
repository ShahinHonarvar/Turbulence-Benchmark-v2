def find_original_set(*args):
    sets = sorted(args, key=len)
    for i in range(1, len(sets)):
        if not sets[i - 1].issubset(sets[i]):
            return sets[i - 1]
    return sets[-1]