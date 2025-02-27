def filter_chars(s):
    chars_to_remove = set((c for c in s if s.index(c) >= 42 and s.index(c) <= 97 and ('*' <= c <= 'b')))
    return ''.join((c for c in s if c not in chars_to_remove))