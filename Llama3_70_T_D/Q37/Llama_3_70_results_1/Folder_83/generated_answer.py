def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(29, 80) if 'K' <= s[i] <= 'z'))
    return ''.join((c for c in s if c not in chars_to_remove))