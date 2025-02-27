def filter_chars(s):
    chars_to_remove = set((c for c in s[14:75] if '9' < c < 'K'))
    return ''.join((c for c in s if c not in chars_to_remove))