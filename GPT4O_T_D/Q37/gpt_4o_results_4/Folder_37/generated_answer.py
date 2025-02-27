def filter_chars(s):
    filtered_chars = {c for c in s[17:64] if 'O' <= c <= '^'}
    return ''.join((c for c in s if c not in filtered_chars))