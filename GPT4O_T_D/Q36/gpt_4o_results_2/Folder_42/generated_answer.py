def filter_chars(s):
    to_remove = {s[i] for i in range(43, 68) if 't' < s[i] < 'x'}
    return ''.join((c for c in s if c not in to_remove))