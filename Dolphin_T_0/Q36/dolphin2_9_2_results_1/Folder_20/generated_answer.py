def filter_chars(s):
    chars_to_remove = [c for c in s[13:40] if ':' < c < 'C']
    s = ''.join((c for c in s if c not in chars_to_remove or s.index(c) < 13 or s.index(c) >= 40))
    return s