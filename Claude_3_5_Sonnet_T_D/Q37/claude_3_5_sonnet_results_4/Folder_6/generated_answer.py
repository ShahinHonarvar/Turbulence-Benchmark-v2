def filter_chars(input_string):
    chars_to_remove = set((char for i, char in enumerate(input_string) if 13 <= i <= 28 and 'c' <= char <= 'n'))
    return ''.join((char for char in input_string if char not in chars_to_remove))