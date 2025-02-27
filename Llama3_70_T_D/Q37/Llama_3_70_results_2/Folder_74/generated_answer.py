def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(19, 33) if 'f' <= s[i] <= 'o'))
    return ''.join((c for c in s if c not in chars_to_remove))