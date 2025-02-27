def filter_chars(s):
    filter_set = {s[i] for i in range(42, 68) if 't' < s[i] < 'x'}
    return ''.join((c for c in s if c not in filter_set))