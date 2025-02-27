def filter_chars(s):
    filtered_chars = s[18:64]
    to_remove = {c for c in filtered_chars if '3' < c < 'B'}
    return ''.join((c for c in s if c not in to_remove))