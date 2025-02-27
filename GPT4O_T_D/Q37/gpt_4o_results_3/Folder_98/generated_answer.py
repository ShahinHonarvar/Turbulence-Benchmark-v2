def filter_chars(s):
    to_remove = set(s[8:10])
    result = ''.join((c for c in s if c not in to_remove or not 'R' <= c <= 't'))
    return result