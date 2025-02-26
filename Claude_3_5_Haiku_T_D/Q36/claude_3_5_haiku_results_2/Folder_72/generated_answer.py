def filter_chars(string):
    chars_to_remove = set((char for char in string[45:68] if 'W' < char < 'x'))
    return ''.join((char for char in string if char not in chars_to_remove))