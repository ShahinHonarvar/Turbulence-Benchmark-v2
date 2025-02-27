def remove_repeat_chars(input_string):
    for char in set(input_string[1:4]):
        if input_string[1:4].count(char) > 1:
            input_string = input_string.replace(char, '', 1)
    return input_string