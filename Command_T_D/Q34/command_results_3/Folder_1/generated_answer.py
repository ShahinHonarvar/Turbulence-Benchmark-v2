def find_original_set(S):
    S.sort()
    res = set()
    for x in S:
        res.update(x)
    for x in S:
        res.update(x)
    return res