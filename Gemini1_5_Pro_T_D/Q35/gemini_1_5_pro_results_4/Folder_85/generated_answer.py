def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(1, min(8, len(s) - 1)):
        c = s[i]
        if c in seen:
            repeated.add(c)
        else:
            seen.add(c)
    t = ''
    for c in s:
        if c not in repeated:
            t += c
    return t