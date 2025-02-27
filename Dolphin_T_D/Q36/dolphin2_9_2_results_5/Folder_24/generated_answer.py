def filter_chars(string):
    chars_to_remove = [c for c in string[10:15] if 't' < c < 'v']
    return ''.join((char for char in string if char not in chars_to_remove))