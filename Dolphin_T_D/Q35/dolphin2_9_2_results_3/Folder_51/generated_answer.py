def remove_repeat_chars(input_string):
    chars_to_remove = [char for char in input_string[6:9] if input_string.count(char) > 1]
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string