def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, c in enumerate(s):
        if i > 0 and i < 7 and (s.count(c) > 1):
            if c not in seen:
                seen.add(c)
        else:
            new_s += c
    return new_s