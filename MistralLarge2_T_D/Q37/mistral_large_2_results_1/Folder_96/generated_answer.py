def filter_chars(s):
    target_chars = {c for i, c in enumerate(s) if 86 <= i <= 92 and '!' <= c <= 's'}
    return ''.join((c for c in s if c not in target_chars))