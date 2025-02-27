def filter_chars(s):
    to_remove = {s[i] for i in range(31, 73) if 'M' < s[i] < 'j'}
    return ''.join((c for c in s if c not in to_remove))