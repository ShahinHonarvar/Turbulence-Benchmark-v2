def filter_chars(s):
    target_chars = set((c for c in s[4:8] if '?' < c < 'k'))
    return ''.join((c for c in s if c not in target_chars))