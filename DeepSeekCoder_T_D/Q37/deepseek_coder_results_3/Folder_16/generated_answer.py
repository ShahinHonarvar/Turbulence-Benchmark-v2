def filter_chars(s):
    filtered_chars = set(s[225:382]) & set(('D' <= c <= 'Y' for c in s[225:382]))
    return ''.join((c for c in s if c not in filtered_chars))