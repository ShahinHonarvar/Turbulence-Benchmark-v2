def filter_chars(input_string):
    for char in input_string[19:93]:
        if char >= '8' and char <= 'm':
            input_string = input_string.replace(char, '')
    return input_string