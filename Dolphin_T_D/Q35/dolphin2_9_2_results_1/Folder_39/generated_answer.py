def remove_repeat_chars(s):
    chars_to_remove = [c for c in s[44:91] if s.count(c) > 1]
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s