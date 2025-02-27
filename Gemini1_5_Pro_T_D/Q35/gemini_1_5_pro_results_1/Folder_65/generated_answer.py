def remove_repeat_chars(s):
    seen = set()
    res = ''
    for i, c in enumerate(s):
        if 51 < i < 76:
            if c in seen:
                continue
            else:
                seen.add(c)
        res += c
    return res