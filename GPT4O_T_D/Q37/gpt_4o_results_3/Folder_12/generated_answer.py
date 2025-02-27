def filter_chars(s):
    to_remove = {c for c in set(s[19:91]) if 'F' <= c <= 'h'}
    return ''.join((c for c in s if c not in to_remove))