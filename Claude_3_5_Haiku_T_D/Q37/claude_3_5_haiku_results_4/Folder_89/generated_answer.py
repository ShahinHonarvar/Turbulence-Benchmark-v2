def filter_chars(input_str):
    chars_to_remove = set((char for char in input_str[11:33] if '!' <= char <= '@'))
    return ''.join((char for char in input_str if char not in chars_to_remove))