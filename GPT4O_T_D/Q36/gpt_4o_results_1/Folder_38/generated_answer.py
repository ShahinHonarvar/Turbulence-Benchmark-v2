def filter_chars(s):
    to_remove = set(filter(lambda c: '+' < c < 'l', s[45:48]))
    return ''.join((c for c in s if c not in to_remove))