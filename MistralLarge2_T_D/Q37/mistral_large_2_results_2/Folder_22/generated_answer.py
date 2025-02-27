def filter_chars(s):
    chars_to_remove = set((s[i] for i in range(33, 71) if '7' <= s[i] <= 'k'))
    return ''.join((c for c in s if c not in chars_to_remove))