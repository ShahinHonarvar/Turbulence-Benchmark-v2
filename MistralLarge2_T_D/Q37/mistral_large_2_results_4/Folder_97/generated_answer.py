def filter_chars(s):
    chars_to_remove = {ch for ch in s[227:236] if 'D' <= ch <= 'u'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))