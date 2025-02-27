def filter_chars(s):
    chars = {s[i] for i in range(344, 874)}
    new_chars = {c for c in chars if 'f' < c < '~'}
    s = [c for c in s if c not in new_chars]
    return ''.join(s)