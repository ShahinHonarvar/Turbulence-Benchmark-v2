def filter_chars(s):
    indices_range = s[27:86]
    chars_to_remove = {char for char in indices_range if 'c' <= char <= 'i'}
    return ''.join((char for char in s if char not in chars_to_remove))