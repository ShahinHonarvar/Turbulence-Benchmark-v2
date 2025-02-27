def remove_repeat_chars(s):
    seen = set()
    new_s = ''
    for i, c in enumerate(s):
        if 11 < i < 76:
            if c in seen:
                continue
            if s.count(c) > 1:
                seen.add(c)
                continue
        new_s += c
    return new_s