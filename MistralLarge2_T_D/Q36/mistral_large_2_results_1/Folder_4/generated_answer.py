def filter_chars(s):
    chars_to_remove = set((c for c in s[42:67] if '6' < c < 'g'))
    return ''.join((c for c in s if c not in chars_to_remove))