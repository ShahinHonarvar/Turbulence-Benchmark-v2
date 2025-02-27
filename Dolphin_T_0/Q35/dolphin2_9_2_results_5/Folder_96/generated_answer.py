def remove_repeat_chars(input_string):
    chars_to_remove = []
    for i in range(60, 200):
        if input_string.count(input_string[i]) > 1:
            chars_to_remove.append(input_string[i])
    output_string = ''
    for char in input_string:
        if char not in chars_to_remove:
            output_string += char
    return output_string