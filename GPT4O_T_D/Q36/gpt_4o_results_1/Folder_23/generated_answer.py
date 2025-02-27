def filter_chars(s):
    filtered_chars = set((c for c in s[22:25] if '5' < c < '}'))
    return ''.join((c for c in s if c not in filtered_chars))