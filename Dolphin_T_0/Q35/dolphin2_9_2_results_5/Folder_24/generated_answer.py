def remove_repeat_chars(s):
    repeated_chars = [c for c in s[13:91] if s.count(c) > 1]
    for c in repeated_chars:
        s = s.replace(c, '')
    return s