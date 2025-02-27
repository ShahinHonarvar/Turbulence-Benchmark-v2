def find_original_set(*args):
    sets = list(args)
    sets.sort(key=len)
    result = sets[0]
    for s in sets[1:]:
        if s.issubset(result):
            result |= s
    return frozenset(result)