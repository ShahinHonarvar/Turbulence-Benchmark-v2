def filter_chars(s):
    chars_remove = [c for c in s[13:29] if 'c' <= c <= 'n']
    return ''.join([c for c in s if c not in chars_remove])