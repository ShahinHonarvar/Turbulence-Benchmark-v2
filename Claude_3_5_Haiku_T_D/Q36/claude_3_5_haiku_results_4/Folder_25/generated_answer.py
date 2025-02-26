def filter_chars(string):
    chars_to_remove = set((char for char in string[25:37] if 'A' < char < 'h'))
    return ''.join((char for char in string if char not in chars_to_remove))