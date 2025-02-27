def filter_chars(s):
    chars_to_remove = {char for char in s[45:57] if 'F' < char < 'n'}
    return ''.join((char for char in s if char not in chars_to_remove))