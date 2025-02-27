def filter_chars(s):
    chars_to_remove = {ch for i, ch in enumerate(s) if 5 <= i <= 6 and 'G' <= ch <= 'p'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))