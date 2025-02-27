def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 7 <= i <= 9 and '6' <= char <= 'w'}
    return ''.join((char for char in s if char not in chars_to_remove))