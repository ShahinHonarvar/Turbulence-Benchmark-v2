def filter_chars(s):
    chars_to_remove = set((c for c in s[259:503] if ',' <= c <= '3'))
    return ''.join((c for c in s if c not in chars_to_remove))