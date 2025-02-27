def filter_chars(s):
    to_remove = set(s[15:85]) & set('JKL')
    return ''.join((c for c in s if c not in to_remove))