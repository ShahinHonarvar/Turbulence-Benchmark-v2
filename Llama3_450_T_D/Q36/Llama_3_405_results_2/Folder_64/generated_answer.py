def filter_chars(s):
    chars_to_remove = [c for c in s[1:7] if '3' < c < '^']
    return ''.join((c for c in s if c not in chars_to_remove))