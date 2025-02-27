def remove_repeat_chars(input_string):
    chars_to_remove = set()
    for i in range(81, 86):
        char_count = input_string.count(input_string[i])
        if char_count > 1:
            chars_to_remove.add(input_string[i])
    output_string = ''
    for char in input_string:
        if char not in chars_to_remove:
            output_string += char
    return output_string