def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i, c in enumerate(s):
        if 20 < i < 43:
            if c in seen:
                repeated.add(c)
            else:
                seen.add(c)
    res = []
    for c in s:
        if c not in repeated:
            res.append(c)
    return ''.join(res)