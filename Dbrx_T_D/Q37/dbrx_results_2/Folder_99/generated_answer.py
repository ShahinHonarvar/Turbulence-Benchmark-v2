def filter_chars(s):
    chars_to_remove = set(range(ord('T'), ord('h') + 1)) & set((ord(c) for c in s[373:901]))
    return ''.join((c for c in s if ord(c) not in chars_to_remove))