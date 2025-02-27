def filter_chars(s):
    remove_chars = {c for c in s[45:48] if '+' < c < 'l'}
    result = ''.join((c for c in s if c not in remove_chars))
    return result