def filter_chars(s):
    to_remove = {ch for i, ch in enumerate(s) if 12 <= i <= 25 and 'P' <= ch <= 'x'}
    return ''.join((ch for ch in s if ch not in to_remove))