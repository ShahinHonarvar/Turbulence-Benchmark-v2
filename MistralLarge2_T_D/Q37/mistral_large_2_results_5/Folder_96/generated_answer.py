def filter_chars(s):
    to_remove = set((s[i] for i in range(86, 93) if '!' <= s[i] <= 's'))
    return ''.join((c for c in s if c not in to_remove))