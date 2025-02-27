def filter_chars(s):
    to_remove = {c for c in s[44:83] if ':' < c < 'Q'}
    return ''.join((c for c in s if c not in to_remove))