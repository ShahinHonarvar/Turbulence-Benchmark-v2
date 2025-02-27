def filter_chars(s):
    chars_to_remove = [c for c in s[19:69] if ord('<') < ord(c) < ord('C')]
    for c in chars_to_remove:
        s = s.replace(c, '', 1)
    return s