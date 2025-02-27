def filter_chars(s):
    chars_to_remove = set(s[52:88]).intersection(set((chr(i) for i in range(ord('&') + 1, ord('c')))))
    return ''.join((c for c in s if c not in chars_to_remove))