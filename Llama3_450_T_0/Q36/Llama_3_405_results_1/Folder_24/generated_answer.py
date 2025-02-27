def filter_chars(s):
    chars_to_remove = [c for c in s[10:15] if 't' < c < 'v']
    return ''.join([c for c in s if c not in chars_to_remove])