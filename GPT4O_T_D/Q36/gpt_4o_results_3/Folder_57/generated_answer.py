def filter_chars(s):
    to_remove = {s[i] for i in range(71, 74) if 'A' < s[i] < 'U'}
    return ''.join((c for c in s if c not in to_remove))