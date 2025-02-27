def remove_repeat_chars(input_string):
    for char in set(input_string[45:48]):
        if input_string[45:48].count(char) > 1:
            input_string = input_string.replace(char, '', input_string[45:48].count(char))
    return input_string