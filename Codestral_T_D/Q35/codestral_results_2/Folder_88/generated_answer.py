def remove_repeat_chars(input_string):
    chars_to_remove = set((char for char in input_string[3:9] if input_string.count(char) > 1))
    return ''.join((char for char in input_string if char not in chars_to_remove))