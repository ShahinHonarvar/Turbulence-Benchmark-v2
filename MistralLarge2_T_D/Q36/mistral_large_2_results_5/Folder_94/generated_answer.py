def filter_chars(s):
    chars_to_remove = {char for char in s[15:85] if 'I' < char < 'M'}
    return ''.join((char for char in s if char not in chars_to_remove))