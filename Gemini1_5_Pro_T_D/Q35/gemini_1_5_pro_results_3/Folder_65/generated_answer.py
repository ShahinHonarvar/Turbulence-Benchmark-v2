def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(51, 76):
        if s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    t = ''
    for c in s:
        if c not in repeated:
            t += c
    return t