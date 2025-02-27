def filter_chars(s):
    chars_to_remove = [c for c in s if 27 <= s.index(c) <= 29 and ';' <= c <= 'b']
    return ''.join([c for c in s if c not in chars_to_remove])