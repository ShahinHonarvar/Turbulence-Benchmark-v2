def remove_repeat_chars(input_string):
    return ''.join((char for char in input_string if char not in input_string[20:43] or input_string.index(char) >= 43))