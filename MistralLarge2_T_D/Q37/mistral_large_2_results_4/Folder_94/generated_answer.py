def filter_chars(s):
    to_remove = set((s[i] for i in range(51, 97) if 'X' <= s[i] <= 'p'))
    return ''.join((c for c in s if c not in to_remove))