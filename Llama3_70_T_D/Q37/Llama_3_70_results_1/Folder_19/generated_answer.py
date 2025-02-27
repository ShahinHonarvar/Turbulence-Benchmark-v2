def filter_chars(s):
    to_remove = set((s[i] for i in range(35, 90) if 'E' <= s[i] <= 't'))
    return ''.join((c for c in s if c not in to_remove))