def filter_chars(s):
    chars_to_remove = [c for c in s[41:56] if 'Z' < c < 'c']
    return ''.join((c for c in s if c not in chars_to_remove))