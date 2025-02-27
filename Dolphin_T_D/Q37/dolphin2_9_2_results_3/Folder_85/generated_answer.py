def filter_chars(s):
    chars_to_remove = [c for c in s if 28 <= s.index(c) <= 65 and 'O' <= c <= 'd']
    return ''.join([c for c in s if c not in chars_to_remove])