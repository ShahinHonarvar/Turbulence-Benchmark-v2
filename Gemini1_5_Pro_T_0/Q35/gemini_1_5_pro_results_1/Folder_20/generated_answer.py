def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 27 < i < 96 and s.count(c) > 1:
            if c not in seen:
                seen.add(c)
        else:
            result += c
    return result