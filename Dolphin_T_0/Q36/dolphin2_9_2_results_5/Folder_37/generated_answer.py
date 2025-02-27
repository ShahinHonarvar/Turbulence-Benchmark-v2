def filter_chars(s):
    chars_to_remove = [c for c in s[44:59] if c > '/' and c < '6']
    s = ''.join([c for c in s if c not in chars_to_remove])
    return s