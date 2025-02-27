def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(14, 70):
        c = s[i]
        if c in seen:
            repeated.add(c)
        seen.add(c)
    res = []
    for c in s:
        if c not in repeated:
            res.append(c)
    return ''.join(res)