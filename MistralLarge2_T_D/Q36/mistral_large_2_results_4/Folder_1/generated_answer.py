def filter_chars(s):
    to_remove = {s[i] for i in range(69, 87) if 'I' > s[i] > '#'}
    return ''.join((c for c in s if c not in to_remove))