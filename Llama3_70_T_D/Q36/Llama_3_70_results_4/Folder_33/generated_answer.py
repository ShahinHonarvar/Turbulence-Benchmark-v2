def filter_chars(s):
    chars_to_remove = set(s[300:418]).intersection(set((chr(i) for i in range(ord('9') + 1, ord('P')))))
    return ''.join((c for c in s if c not in chars_to_remove))