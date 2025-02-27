def filter_chars(s):
    if len(s) <= 4:
        return s
    to_filter = set((c for c in s[4:8] if '?' < c < 'k'))
    return ''.join((c for c in s if c not in to_filter))