def remove_repeat_chars(input_string):
    for char in input_string:
        if input_string.count(char) > 1 and ord(char) > 27 and (ord(char) < 96):
            input_string = input_string.replace(char, '')
    return input_string