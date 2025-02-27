def find_original_set(*sets):
    res = {}
    for s in sets:
        for i in s:
            if i not in res:
                res[i] = True
    return set(res.keys())