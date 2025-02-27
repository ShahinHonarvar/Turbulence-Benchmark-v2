def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 28 <= i <= 65 and 'O' <= char <= 'd'}
    return ''.join((char for char in s if char not in chars_to_remove))