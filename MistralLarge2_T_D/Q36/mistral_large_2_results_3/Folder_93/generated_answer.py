def filter_chars(s):
    chars_to_remove = set((c for c in s[52:88] if '&' < c < 'c'))
    return ''.join((c for c in s if c not in chars_to_remove))