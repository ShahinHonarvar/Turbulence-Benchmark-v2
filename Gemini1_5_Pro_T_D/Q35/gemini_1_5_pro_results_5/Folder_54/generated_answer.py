def remove_repeat_chars(s):
    seen = set()
    repeats = set()
    for i in range(35, 64):
        c = s[i]
        if c in seen:
            repeats.add(c)
        else:
            seen.add(c)
    t = ''
    for c in s:
        if c not in repeats:
            t += c
    return t