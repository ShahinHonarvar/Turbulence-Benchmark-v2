def filter_chars(s):
    to_remove = {s[i] for i in range(344, 874) if 'f' < s[i] < '~'}
    return ''.join((ch for ch in s if ch not in to_remove))