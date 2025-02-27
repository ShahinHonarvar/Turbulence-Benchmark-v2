def filter_chars(s):
    chars_to_remove = [c for c in s if 72 <= s.index(c) <= 94 and '.' <= c <= 'b']
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s