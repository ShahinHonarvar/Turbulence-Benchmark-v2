def filter_chars(string):
    chars_to_remove = set((char for char in string[44:69] if 'B' < char < 'r'))
    return ''.join((char for char in string if char not in chars_to_remove))