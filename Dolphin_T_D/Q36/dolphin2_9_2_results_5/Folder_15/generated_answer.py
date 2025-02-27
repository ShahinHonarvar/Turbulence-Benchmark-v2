def filter_chars(string):
    chars_to_remove = [char for char in string[2:7] if 'h' < char < 'k']
    return ''.join((char for char in string if char not in chars_to_remove))