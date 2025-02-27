def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 12 <= i <= 88 and '&' <= char <= 'v'}
    return ''.join((char for char in s if char not in chars_to_remove))