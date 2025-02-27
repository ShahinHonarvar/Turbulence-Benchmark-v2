def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(55, 84):
        c = s[i]
        if c in seen:
            repeats.add(c)
        else:
            seen.add(c)
    res = []
    for c in s:
        if c not in repeats:
            res.append(c)
    return ''.join(res)