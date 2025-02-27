def remove_repeat_chars(input_string):
    chars_to_remove = []
    for i in range(len(input_string)):
        if i > 0 and i < 3:
            if input_string[i] in input_string[i - 1]:
                chars_to_remove.append(input_string[i])
    for char in chars_to_remove:
        input_string = input_string.replace(char, '', 1)
    return input_string