def remove_repeat_chars(input_string):
    for char in set(input_string[16:88]):
        if input_string[16:88].count(char) > 1:
            input_string = input_string.replace(char, '', input_string[16:88].index(char))
            input_string = input_string.replace(char, '', input_string[16:88].index(char, input_string[16:88].index(char) + 1))
    return input_string