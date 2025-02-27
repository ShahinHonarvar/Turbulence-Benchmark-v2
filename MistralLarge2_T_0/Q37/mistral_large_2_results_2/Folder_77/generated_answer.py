def filter_chars(s):
    chars_to_remove = set((c for c in s[384:412] if '/' <= c <= '8'))
    return ''.join((c for c in s if c not in chars_to_remove))