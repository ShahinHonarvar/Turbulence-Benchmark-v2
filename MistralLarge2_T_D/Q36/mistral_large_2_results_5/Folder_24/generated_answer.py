def filter_chars(s):
    to_remove = {s[i] for i in range(11, 15) if 't' < s[i] < 'v'}
    return ''.join((c for c in s if c not in to_remove))