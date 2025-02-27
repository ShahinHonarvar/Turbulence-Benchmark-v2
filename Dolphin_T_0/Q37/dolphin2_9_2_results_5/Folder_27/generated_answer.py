def filter_chars(input_string):
    for char in input_string:
        if 43 <= input_string.index(char) <= 80 and (char >= '=' and char <= 'E'):
            input_string = input_string.replace(char, '')
    return input_string