def filter_chars(s):
    chars_to_remove = {ch for i, ch in enumerate(s) if 31 <= i <= 38 and ';' <= ch <= 'g'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))