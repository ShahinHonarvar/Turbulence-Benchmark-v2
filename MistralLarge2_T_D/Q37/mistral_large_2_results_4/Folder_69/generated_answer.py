def filter_chars(s):
    to_remove = {c for i, c in enumerate(s) if 114 <= i <= 639 and '!' <= c <= 'x'}
    return ''.join((c for c in s if c not in to_remove))