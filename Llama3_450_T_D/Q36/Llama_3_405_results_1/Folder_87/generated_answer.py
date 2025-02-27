def filter_chars(s):
    chars_to_remove = set(s[32:61]).intersection(set((chr(i) for i in range(ord('3') + 1, ord('D')))))
    return ''.join((c for c in s if c not in chars_to_remove))