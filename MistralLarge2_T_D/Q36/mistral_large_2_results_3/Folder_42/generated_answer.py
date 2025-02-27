def filter_chars(s):
    to_remove = {ch for ch in s[42:68] if 't' < ch < 'x'}
    return ''.join((ch for ch in s if ch not in to_remove))