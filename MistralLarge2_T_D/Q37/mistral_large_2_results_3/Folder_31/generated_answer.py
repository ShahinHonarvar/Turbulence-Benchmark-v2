def filter_chars(s):
    to_remove = set((s[i] for i in range(57, 97) if '<' <= s[i] <= 'w'))
    return ''.join((c for c in s if c not in to_remove))