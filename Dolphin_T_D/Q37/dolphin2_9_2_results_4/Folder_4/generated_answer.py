def filter_chars(s):
    to_remove = [c for c in s[19:34] if c >= 'S' and c <= '{']
    return ''.join([c for c in s if c not in to_remove])