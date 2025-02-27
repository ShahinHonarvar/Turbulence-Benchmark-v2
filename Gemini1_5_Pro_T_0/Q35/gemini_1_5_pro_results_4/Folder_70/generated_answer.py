def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(43, 70):
        c = s[i]
        if c in seen:
            repeated.add(c)
        seen.add(c)
    t = ''
    for c in s:
        if c not in repeated:
            t += c
    return t