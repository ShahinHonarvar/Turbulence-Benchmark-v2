def filter_chars(s):
    to_remove = set((c for c in s[300:418] if '9' < c < 'P'))
    return ''.join((c for c in s if c not in to_remove))