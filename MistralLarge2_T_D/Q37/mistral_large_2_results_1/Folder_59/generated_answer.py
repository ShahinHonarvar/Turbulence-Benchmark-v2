def filter_chars(s):
    chars_to_remove = {ch for ch in s[2:5] if '5' <= ch <= '_'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))