def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i, c in enumerate(s):
        if 35 < i < 64 and s.count(c) > 1:
            if c not in seen:
                seen.add(c)
        else:
            res += c
    return res