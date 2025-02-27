def filter_chars(input_string):
    for char in range(ord('9') + 1, ord('P')):
        input_string = input_string.replace(chr(char), '')
    return input_string