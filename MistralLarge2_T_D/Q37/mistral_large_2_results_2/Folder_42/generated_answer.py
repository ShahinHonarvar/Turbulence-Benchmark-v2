def filter_chars(s):
    chars_to_remove = {ch for ch in s[73:75] if 'U' <= ch <= 'l'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))