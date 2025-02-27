def filter_chars(s):
    chars_to_remove = set(s[7:10])
    chars_to_remove = {char for char in chars_to_remove if '6' <= char <= 'w'}
    return ''.join((char for char in s if char not in chars_to_remove))