def filter_chars(s):
    to_filter = {c for c in s[24:83] if '5' <= c <= '<'}
    return ''.join((c for c in s if c not in to_filter))