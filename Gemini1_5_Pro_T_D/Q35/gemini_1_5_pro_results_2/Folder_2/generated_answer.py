def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(72, 93):
        if i < len(s) and s[i] in seen:
            repeats.add(s[i])
        else:
            seen.add(s[i])
    res = []
    for c in s:
        if c not in repeats:
            res.append(c)
    return ''.join(res)