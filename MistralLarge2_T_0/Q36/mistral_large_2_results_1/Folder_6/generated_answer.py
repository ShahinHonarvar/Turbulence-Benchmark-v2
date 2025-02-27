def filter_chars(s):
    chars_to_remove = set((c for c in s[31:70] if 'B' < c < 'v'))
    return ''.join((c for c in s if c not in chars_to_remove))