def filter_chars(s):
    to_remove = [c for c in s[5:8] if '1' < c < 'J']
    return ''.join((c for c in s if c not in to_remove))