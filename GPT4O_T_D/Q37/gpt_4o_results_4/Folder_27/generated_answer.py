def filter_chars(s):
    to_remove = set((c for c in s[43:81] if '=' <= c <= 'E'))
    return ''.join((c for c in s if c not in to_remove))