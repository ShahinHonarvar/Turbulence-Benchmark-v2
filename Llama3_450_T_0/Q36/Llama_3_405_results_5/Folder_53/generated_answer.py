def filter_chars(s):
    chars_to_remove = set(s[90:97]).intersection(set((chr(i) for i in range(ord('j') + 1, ord('w')))))
    return ''.join((c for c in s if c not in chars_to_remove))