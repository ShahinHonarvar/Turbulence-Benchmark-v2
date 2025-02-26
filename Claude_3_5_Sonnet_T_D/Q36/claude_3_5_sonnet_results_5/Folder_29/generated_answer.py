def filter_chars(input_string):
    chars_to_remove = set((char for char in input_string[47:68] if 'H' < char < 's'))
    return ''.join((char for char in input_string if char not in chars_to_remove))