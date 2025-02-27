def filter_chars(s):
    indices_range = range(384, 412)
    to_remove = {c for i, c in enumerate(s) if i in indices_range and '/' <= c <= '8'}
    return ''.join((c for c in s if c not in to_remove))