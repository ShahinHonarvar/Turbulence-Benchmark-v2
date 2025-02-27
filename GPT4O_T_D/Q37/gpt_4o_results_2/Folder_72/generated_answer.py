def filter_chars(s):
    filtered_chars = {c for c in s[35:52] if 'H' <= c <= 's'}
    return ''.join((c for c in s if c not in filtered_chars))