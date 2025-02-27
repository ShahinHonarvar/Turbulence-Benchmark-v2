def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(43, 70):
        c = s[i]
        if c in seen:
            repeats.add(c)
        seen.add(c)
    res = []
    for c in s:
        if c not in repeats:
            res.append(c)
    return ''.join(res)