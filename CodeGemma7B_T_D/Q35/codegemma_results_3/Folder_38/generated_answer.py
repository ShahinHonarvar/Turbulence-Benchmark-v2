def remove_repeat_chars(s):
    seen = set()
    for i, c in enumerate(s):
        if i in range(36, 85) and c in seen:
            s = s.replace(c, '')
        else:
            seen.add(c)
    return s