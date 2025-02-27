def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 20 <= i <= 62 and 'i' <= char <= 'k'}
    return ''.join((char for char in s if char not in chars_to_remove))