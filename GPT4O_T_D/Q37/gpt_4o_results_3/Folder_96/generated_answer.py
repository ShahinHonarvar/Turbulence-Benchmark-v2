def filter_chars(s):
    if len(s) < 93:
        return s
    filtered_chars = {c for c in s[86:93] if '!' <= c <= 's'}
    return ''.join((c for c in s if c not in filtered_chars))