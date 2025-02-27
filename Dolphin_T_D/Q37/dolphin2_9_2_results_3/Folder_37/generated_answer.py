def filter_chars(s):
    chars_to_remove = [c for c in s[17:64] if c >= 'O' and c <= '^']
    s = ''.join((c for c in s if c not in chars_to_remove))
    return s