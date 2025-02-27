def filter_chars(s):
    to_remove = [c for c in s[513:878] if '?' <= c <= 'n']
    for c in to_remove:
        s = s.replace(c, '')
    return s