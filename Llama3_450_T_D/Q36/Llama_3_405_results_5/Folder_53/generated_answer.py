def filter_chars(s):
    chars_to_remove = set(s[91:97]).intersection(set((chr(i) for i in range(ord('k'), ord('w')))))
    return ''.join((c for c in s if c not in chars_to_remove))