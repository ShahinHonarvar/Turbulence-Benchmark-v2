def filter_chars(s):
    indices_range = s[35:41]
    chars_to_remove = {char for char in indices_range if ')' <= char <= 'l'}
    return ''.join((char for char in s if char not in chars_to_remove))