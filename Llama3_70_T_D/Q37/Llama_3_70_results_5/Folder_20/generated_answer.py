def filter_chars(input_string):
    output_string = ''
    for char in input_string:
        if not (25 <= ord(char) <= 97 and 'm' <= char <= 'w'):
            output_string += char
    return output_string