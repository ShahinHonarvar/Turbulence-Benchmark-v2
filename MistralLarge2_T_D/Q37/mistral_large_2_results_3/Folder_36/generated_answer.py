def filter_chars(s):
    to_remove = set((s[i] for i in range(259, 503) if ',' <= s[i] <= '3'))
    return ''.join((c for c in s if c not in to_remove))