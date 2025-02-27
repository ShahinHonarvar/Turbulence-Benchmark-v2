def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i, c in enumerate(s):
        if 20 < i < 51:
            if c in seen:
                continue
            elif s[21:51].count(c) > 1:
                seen.add(c)
                continue
        res += c
    return res