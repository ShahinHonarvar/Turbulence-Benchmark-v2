def filter_chars(s):
    chars_to_remove = set((s[332:713][c] for c in range(len(s[332:713])) if 'M' < s[332:713][c] < '_'))
    return ''.join((c for c in s if c not in chars_to_remove))