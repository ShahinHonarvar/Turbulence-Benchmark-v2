def filter_chars(s):
    target_chars = set()
    if len(s) > 43:
        target_chars = {c for c in s[43:81] if '=' <= c <= 'E'}
    return ''.join((c for c in s if c not in target_chars))