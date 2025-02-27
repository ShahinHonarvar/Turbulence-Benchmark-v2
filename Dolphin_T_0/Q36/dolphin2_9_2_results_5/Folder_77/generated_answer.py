def filter_chars(string):
    chars_to_remove = [char for char in string[221:420] if '-' < char < 'v']
    return ''.join((char for char in string if char not in chars_to_remove))