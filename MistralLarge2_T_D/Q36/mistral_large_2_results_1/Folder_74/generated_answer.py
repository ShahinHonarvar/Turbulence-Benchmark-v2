def filter_chars(s):
    chars_to_remove = {char for char in s[33:36] if '>' < char < 'A'}
    return ''.join((char for char in s if char not in chars_to_remove))