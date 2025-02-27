def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, c in enumerate(s):
        if 38 <= i <= 52:
            if c in seen:
                continue
            elif s[38:52].count(c) > 1:
                seen.add(c)
                continue
            else:
                new_s += c
            continue
        new_s += c
    return new_s