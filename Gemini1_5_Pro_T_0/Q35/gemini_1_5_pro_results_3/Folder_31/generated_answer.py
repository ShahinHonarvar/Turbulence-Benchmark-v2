def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i, c in enumerate(s):
        if 33 < i < 78:
            if c in seen:
                continue
            elif s[33:78].count(c) > 1:
                seen.add(c)
                continue
        res += c
    return res