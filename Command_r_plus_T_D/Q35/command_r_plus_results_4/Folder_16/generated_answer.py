def remove_repeat_chars(s):
    repeat_chars = [c for c in s[90:97] if s.count(c) > 1]
    for c in repeat_chars:
        s = s.replace(c, '')
    return s