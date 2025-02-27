def filter_chars(s):
    to_remove = set((s[i] for i in range(71, 95) if 'K' <= s[i] <= 'a'))
    return ''.join((c for c in s if c not in to_remove))