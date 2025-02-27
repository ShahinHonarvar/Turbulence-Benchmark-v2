def filter_chars(s):
    if len(s) <= 877:
        return s
    remove_chars = {c for c in s[513:878] if '?' <= c <= 'n'}
    return ''.join((c for c in s if c not in remove_chars))