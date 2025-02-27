def find_original_set(*args):
    sets = list(args)
    for s in sets:
        sets = [ss for ss in sets if not s.issubset(ss)]
    return max(sets, key=len) if sets else None