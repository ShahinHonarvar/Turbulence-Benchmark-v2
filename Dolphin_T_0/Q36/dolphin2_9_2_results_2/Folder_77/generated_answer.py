def filter_chars(input_string):
    for char in input_string:
        if 221 <= input_string.index(char) < 419 and '-' < char < 'v':
            input_string = input_string.replace(char, '')
    return input_string