def remove_repeat_chars(s):
    chars = [c for c in s[72:93] if s.count(c) > 1]
    for c in chars:
        s = s.replace(c, '')
    return s