def filter_chars(s):
    to_remove = [c for c in s[513:878] if '?' <= c <= 'n']
    return ''.join((c for c in s if c not in to_remove))