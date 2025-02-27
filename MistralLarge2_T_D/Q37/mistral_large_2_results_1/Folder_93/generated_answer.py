def filter_chars(s):
    chars_to_remove = {char for i, char in enumerate(s) if 38 <= i <= 69 and 'H' <= char <= 'e'}
    return ''.join((char for char in s if char not in chars_to_remove))