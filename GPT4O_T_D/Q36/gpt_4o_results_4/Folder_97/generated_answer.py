def filter_chars(s):
    removal_chars = {ch for ch in set(s[310:591]) if 'S' < ch < 'm'}
    return ''.join((ch for ch in s if ch not in removal_chars))