def find_original_set(*args):
    sets = list(args)
    sets.sort(key=len)
    for i in range(len(sets) - 1):
        for j in range(i + 1, len(sets)):
            if sets[i].issubset(sets[j]):
                sets.remove(sets[i])
    return sets[0]