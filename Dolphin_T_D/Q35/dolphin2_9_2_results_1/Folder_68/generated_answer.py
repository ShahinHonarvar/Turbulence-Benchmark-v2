def remove_repeat_chars(input_string):
    chars_to_remove = []
    for char_index in range(9):
        char = input_string[char_index]
        if input_string.count(char) > 1:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        input_string = input_string.replace(char, '')
    return input_string