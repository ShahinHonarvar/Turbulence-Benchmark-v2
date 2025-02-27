def filter_chars(s):
    to_remove = {ch for i, ch in enumerate(s) if 1 <= i <= 7 and 'L' <= ch <= 'a'}
    return ''.join((ch for ch in s if ch not in to_remove))