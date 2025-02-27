def filter_chars(s):
    if len(s) <= 3:
        return s
    to_filter = set((c for c in s[4:9] if '*' < c < 'E'))
    return ''.join((c for c in s if c not in to_filter))