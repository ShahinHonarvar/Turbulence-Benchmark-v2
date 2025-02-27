def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(63, 85) if 'E' <= chr(i) <= '~'))
    return ''.join((c for c in s if c not in chars_to_remove))