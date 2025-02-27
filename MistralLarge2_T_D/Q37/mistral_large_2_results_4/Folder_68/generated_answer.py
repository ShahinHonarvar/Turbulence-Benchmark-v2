def filter_chars(s):
    to_remove = {s[i] for i in range(7, 10) if '6' <= s[i] <= 'w'}
    return ''.join((c for c in s if c not in to_remove))