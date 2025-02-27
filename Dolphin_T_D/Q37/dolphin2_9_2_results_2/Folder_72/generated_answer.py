def filter_chars(s):
    to_remove = [c for c in s[35:52] if 'H' <= c <= 's']
    return ''.join((c for c in s if c not in to_remove))