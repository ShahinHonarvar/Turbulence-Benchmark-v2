def filter_chars(input_string):
    filtered_string = ''
    for char in input_string:
        if ord(char) > ord('3') and ord(char) < ord('D'):
            filtered_string += ''
        else:
            filtered_string += char
    return filtered_string