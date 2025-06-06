def filter_chars(s):
    chars_to_remove = set(s[49:56]).intersection(set((chr(i) for i in range(ord('I') + 1, ord('a')))))
    return ''.join((c for c in s if c not in chars_to_remove))