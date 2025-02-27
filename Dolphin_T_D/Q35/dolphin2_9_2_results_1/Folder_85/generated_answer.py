def remove_repeat_chars(input_string):
    chars_to_remove = [input_string[i] for i in range(1, 8) if input_string.count(input_string[i]) > 1]
    altered_string = [char for char in input_string if char not in chars_to_remove]
    return ''.join(altered_string)