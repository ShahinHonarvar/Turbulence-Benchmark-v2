def filter_chars(s):
    chars_to_remove = set((c for c in s[32:61] if '3' < c < 'D'))
    return ''.join((c for c in s if c not in chars_to_remove))