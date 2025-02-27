def filter_chars(s):
    to_remove = {c for c in set(s[73:93]) if '<' < c < 'J'}
    return ''.join((c for c in s if c not in to_remove))