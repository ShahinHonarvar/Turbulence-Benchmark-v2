def if_contains_anagrams(strs):
    res = set()
    for s in strs:
        if len(s) >= 3:
            res.add(tuple(sorted(s.lower())))
    res = list(res)
    if len(res) >= len(strs) // 2:
        return True
    else:
        return False