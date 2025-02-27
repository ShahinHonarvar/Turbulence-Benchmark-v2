def filter_chars(s):
    to_remove = {s[i] for i in range(32, 84) if 'm' < s[i] < 'w'}
    return ''.join((c for c in s if c not in to_remove))