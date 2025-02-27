def filter_chars(s):
    remove_chars = set((c for c in s[82:86] if '!' < c < 's'))
    return ''.join((c for c in s if c not in remove_chars))