def remove_repeat_chars(s):
    seen = set()
    repeated = set()
    for i in range(36, 85):
        if s[i] in seen:
            repeated.add(s[i])
        else:
            seen.add(s[i])
    res = []
    for c in s:
        if c not in repeated:
            res.append(c)
    return ''.join(res)