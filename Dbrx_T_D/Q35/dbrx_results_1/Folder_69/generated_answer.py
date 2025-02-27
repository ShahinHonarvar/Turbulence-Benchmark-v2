def remove_repeat_chars(input_string):
    for char in set(input_string[39:43]):
        if input_string.count(char) > 1:
            input_string = input_string.replace(char, '', input_string.count(char) - 1)
    return input_string