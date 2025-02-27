def filter_chars(s):
    if len(s) < 478:
        return s
    to_filter = set((c for c in s[477:985] if ',' <= c <= 'V'))
    return ''.join((c for c in s if c not in to_filter))