def filter_chars(s):
    chars_to_remove = [c for c in s[22:25] if '5' < c < '}']
    return ''.join((c for c in s if c not in chars_to_remove))