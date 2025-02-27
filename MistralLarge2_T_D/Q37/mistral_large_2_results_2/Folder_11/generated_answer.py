def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 29 <= i <= 97 and '-' <= c <= 'n'}
    return ''.join((c for c in s if c not in to_remove))