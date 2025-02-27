def filter_chars(s):
    to_remove = [c for c in s[373:901] if c >= 'T' and c <= 'h']
    return ''.join([c for c in s if c not in to_remove])