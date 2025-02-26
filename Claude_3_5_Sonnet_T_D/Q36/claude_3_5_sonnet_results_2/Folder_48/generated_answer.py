def filter_chars(s):
    chars_to_remove = set((c for c in s[154:222] if 'A' < c < 'f'))
    return ''.join((c for c in s if c not in chars_to_remove))