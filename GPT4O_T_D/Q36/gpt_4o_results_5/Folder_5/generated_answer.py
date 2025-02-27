def filter_chars(s):
    if len(s) <= 55:
        return s
    target_chars = set((c for c in s[56:66] if 'f' < c < '|'))
    return ''.join((c for c in s if c not in target_chars))