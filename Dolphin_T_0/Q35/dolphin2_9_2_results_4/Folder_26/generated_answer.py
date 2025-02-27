def remove_repeat_chars(input_string):
    chars_to_remove = [char for char in input_string[68:99] if input_string.count(char) > 1]
    new_string = ''
    for char in input_string:
        if char not in chars_to_remove:
            new_string += char
    return new_string