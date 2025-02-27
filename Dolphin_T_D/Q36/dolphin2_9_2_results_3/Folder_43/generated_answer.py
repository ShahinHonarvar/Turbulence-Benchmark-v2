def filter_chars(s):
    to_remove = [c for c in s[27:75] if 'A' < c < 'i']
    return ''.join([c for c in s if c not in to_remove])