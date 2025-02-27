def if_contains_anagrams(strings):
    internals = {}
    for s in strings:
        n = len(s)
        key = sorted(s.lower())
        if key in internals and internals[key] == n:
            return False
        internals[key] = n
    return True