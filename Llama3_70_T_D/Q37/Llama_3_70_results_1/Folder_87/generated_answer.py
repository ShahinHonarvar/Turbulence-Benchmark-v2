def filter_chars(s):
    to_remove = set((s[i] for i in range(18, 82) if 'W' <= s[i] <= '['))
    return ''.join((c for c in s if c not in to_remove))