def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(38, 52):
        if s[i] in seen:
            repeats.add(s[i])
        else:
            seen.add(s[i])
    res = []
    for c in s:
        if c not in repeats:
            res.append(c)
    return ''.join(res)