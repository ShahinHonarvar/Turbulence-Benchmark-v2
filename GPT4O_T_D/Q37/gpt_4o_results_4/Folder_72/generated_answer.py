def filter_chars(s):
    to_remove = {ch for ch in s[35:52] if 'H' <= ch <= 's'}
    return ''.join((ch for ch in s if ch not in to_remove))