def filter_chars(s):
    chars_to_remove = {ch for i, ch in enumerate(s[35:90]) if 'E' <= ch <= 't'}
    return ''.join((ch for ch in s if ch not in chars_to_remove))