def filter_chars(s):
    chars_to_remove = [c for c in s[51:76] if c > '5' and c < 'f']
    return ''.join([c for c in s if c not in chars_to_remove])