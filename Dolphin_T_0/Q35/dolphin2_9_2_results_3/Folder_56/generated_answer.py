def remove_repeat_chars(s):
    chars = set()
    for i in range(7, 10):
        if s[i] in chars:
            s = s[:i] + s[i + 1:]
    for c in chars:
        s = s.replace(c, '')
    return s