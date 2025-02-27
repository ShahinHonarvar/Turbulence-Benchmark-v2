def filter_chars(s):
    to_remove = {ch for idx, ch in enumerate(s) if 13 <= idx <= 28 and 'c' <= ch <= 'n'}
    return ''.join((ch for ch in s if ch not in to_remove))