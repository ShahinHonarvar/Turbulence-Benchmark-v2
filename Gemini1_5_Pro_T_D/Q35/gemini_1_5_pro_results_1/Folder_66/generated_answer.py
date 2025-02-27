def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i, c in enumerate(s):
        if 11 < i < 76:
            if c in seen:
                continue
            seen.add(c)
        result += c
    return result