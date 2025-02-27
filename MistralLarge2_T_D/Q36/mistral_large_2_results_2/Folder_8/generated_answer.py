def filter_chars(string):
    chars_to_remove = {char for char in string[82:93] if '!' < char < '*'}
    return ''.join((char for char in string if char not in chars_to_remove))