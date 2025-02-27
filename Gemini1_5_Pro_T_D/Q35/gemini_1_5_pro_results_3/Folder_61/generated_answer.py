def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if i > 0 and i < 8 and (s.count(c) > 1):
            if c not in seen:
                seen.add(c)
        else:
            result += c
    return result