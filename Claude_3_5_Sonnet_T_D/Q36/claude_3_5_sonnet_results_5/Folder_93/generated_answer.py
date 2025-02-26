def filter_chars(input_string):
    to_remove = set((char for char in input_string[52:88] if '&' < char < 'c'))
    return ''.join((char for char in input_string if char not in to_remove))