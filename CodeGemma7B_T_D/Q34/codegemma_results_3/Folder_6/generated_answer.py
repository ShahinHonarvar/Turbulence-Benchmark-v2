def find_original_set(*args):
    candidates = [set() for _ in range(min(map(len, args)))]
    for arg in args:
        for i, candidate in enumerate(candidates):
            if not candidate.isdisjoint(arg):
                candidates[i] = candidate.union(arg)
    return min(candidates, key=len)