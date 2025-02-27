def find_original_set(*args):
    cand = {}
    for s in args:
        for e in s:
            cand.setdefault(e, set()).add(s)
    return min(cand.values(), key=len)