def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(101, 200):
        if i < len(s) and s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    t = ''
    for c in s:
        if c not in repeated:
            t += c
    return t