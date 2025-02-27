def find_original_set(*args):
    """
    This function takes exactly 453 distinct arguments, each of which is a set of integers.
    The function should return the smallest set such that each of the given arguments is a subset of it.
    """
    sets = list(args)
    sets.sort(key=len)
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            if sets[i].issubset(sets[j]):
                sets.remove(sets[i])
                break
    return sets[0]