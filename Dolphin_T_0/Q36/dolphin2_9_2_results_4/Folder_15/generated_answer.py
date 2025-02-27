def filter_chars(string):
    removed_chars = {char for char in string[2:7] if 'h' < char < 'k'}
    return ''.join((char for char in string if char not in removed_chars))