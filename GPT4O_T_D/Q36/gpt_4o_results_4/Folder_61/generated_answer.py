def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('*') + 1, ord('E'))))
    to_remove = set(s[4:9]).intersection(chars_to_remove)
    return ''.join((c for c in s if c not in to_remove))