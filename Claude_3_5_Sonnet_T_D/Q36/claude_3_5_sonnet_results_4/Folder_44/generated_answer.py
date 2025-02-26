def filter_chars(s):
    chars_to_remove = set((c for c in s[19:64] if '3' < c < 'B'))
    return ''.join((c for c in s if c not in chars_to_remove))