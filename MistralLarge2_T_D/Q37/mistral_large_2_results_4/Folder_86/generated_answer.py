def filter_chars(s):
    to_remove = set((s[i] for i in range(164, 707) if 'O' <= s[i] <= '}'))
    return ''.join((c for c in s if c not in to_remove))