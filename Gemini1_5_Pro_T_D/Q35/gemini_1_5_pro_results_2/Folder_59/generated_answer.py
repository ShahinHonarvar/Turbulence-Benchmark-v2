def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, c in enumerate(s):
        if i > 0 and i < 10 and (c in s[0:i]):
            seen.add(c)
        if c not in seen:
            new_s += c
    return new_s