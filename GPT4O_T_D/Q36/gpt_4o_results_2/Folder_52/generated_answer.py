def filter_chars(s):
    chars_to_remove = set((c for c in s[50:56] if 'I' < c < 'a'))
    return ''.join((c for c in s if c not in chars_to_remove))