def filter_chars(s):
    to_remove = {ch for ch in s[1:6] if ',' < ch < 'f'}
    return ''.join((ch for ch in s if ch not in to_remove))