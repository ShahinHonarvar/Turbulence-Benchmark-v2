def filter_chars(string):
    chars_to_remove = [char for char in string[2:4] if '5' <= char <= '_']
    return ''.join((char for char in string if char not in chars_to_remove))