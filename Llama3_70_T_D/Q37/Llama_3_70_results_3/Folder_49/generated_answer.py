def filter_chars(s):
    chars_to_remove = [c for c in set(s) if ord(c) >= 42 and ord(c) <= 97 and (c >= '*') and (c <= 'b')]
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s