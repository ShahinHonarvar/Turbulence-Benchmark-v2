def filter_chars(s):
    to_remove = {c for c in s[43:67] if '6' < c < 'g'}
    return ''.join((c for c in s if c not in to_remove))