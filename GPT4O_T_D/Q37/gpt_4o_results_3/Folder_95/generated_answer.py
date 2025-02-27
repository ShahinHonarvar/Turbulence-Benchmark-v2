def filter_chars(s):
    filter_range = s[35:41]
    chars_to_remove = {ch for ch in filter_range if ')' <= ch <= 'l'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))