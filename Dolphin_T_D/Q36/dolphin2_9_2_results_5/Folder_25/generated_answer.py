def filter_chars(s):
    chars_to_remove = [c for c in s[24:37] if c > 'A' and c < 'h']
    return ''.join((c for c in s if c not in chars_to_remove))