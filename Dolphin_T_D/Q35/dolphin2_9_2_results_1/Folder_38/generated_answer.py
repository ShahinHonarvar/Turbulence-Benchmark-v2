def remove_repeat_chars(s):
    to_remove = [c for c in s[36:85] if s.count(c, 36, 85) > 1]
    for c in to_remove:
        s = s.replace(c, '')
    return s