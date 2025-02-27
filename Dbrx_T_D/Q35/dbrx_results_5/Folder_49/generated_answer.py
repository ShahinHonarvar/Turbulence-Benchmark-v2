def remove_repeat_chars(input_string):
    for char in set(input_string[90:200]):
        if input_string.count(char) > input_string[90:200].count(char):
            input_string = input_string.replace(char, '', input_string.count(char) - input_string[90:200].count(char))
    return input_string